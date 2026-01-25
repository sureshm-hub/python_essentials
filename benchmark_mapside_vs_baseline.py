#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PySpark benchmark: baseline wordcount vs map-side aggregation wordcount.

Usage:
  spark-submit benchmark_mapside_vs_baseline.py \
      --records 200000 \
      --avg-words 40 \
      --vocab 50000 \
      --partitions 48 \
      --zipf 1.2 \
      --master local[*]

Tip: Open Spark UI at http://localhost:4040 to compare Shuffle Read/Write metrics.
"""

import argparse
import math
import time
import random
from operator import add
from typing import Iterable, Iterator, Tuple

from pyspark.sql import SparkSession


def parse_args():
    p = argparse.ArgumentParser(description="Benchmark map-side aggregation for word count")
    p.add_argument("--records", type=int, default=200_000, help="Number of records (lines) to generate")
    p.add_argument("--avg-words", type=int, default=40, help="Average words per record")
    p.add_argument("--vocab", type=int, default=50_000, help="Vocabulary size")
    p.add_argument("--zipf", type=float, default=1.2, help="Zipf exponent (>=1.0 means skewed)")
    p.add_argument("--partitions", type=int, default=48, help="Number of input partitions")
    p.add_argument("--master", type=str, default=None, help='Override master (e.g. "local[*]")')
    p.add_argument("--seed", type=int, default=42, help="Random seed")
    return p.parse_args()


def make_zipf_weights(vocab_size: int, s: float) -> list:
    # Unnormalized weights ~ 1 / i^s
    weights = [1.0 / (i ** s) for i in range(1, vocab_size + 1)]
    total = sum(weights)
    return [w / total for w in weights]


def gen_lines_in_partition(part_idx: int,
                           num_records_total: int,
                           num_partitions: int,
                           avg_words: int,
                           vocab_size: int,
                           zipf_weights: list,
                           seed: int) -> Iterator[str]:
    # Compute how many records this partition should generate
    base = num_records_total // num_partitions
    extra = 1 if part_idx < (num_records_total % num_partitions) else 0
    n = base + extra
    rnd = random.Random(seed + part_idx)

    # Precompute cumulative weights for efficiency
    # random.choices accepts weights directly; it's efficient enough in CPython 3.8+
    vocab = [f"w{i}" for i in range(1, vocab_size + 1)]

    for _ in range(n):
        k = max(1, int(rnd.gauss(avg_words, max(1.0, avg_words * 0.1))))  # small variance
        words = rnd.choices(vocab, weights=zipf_weights, k=k)
        yield " ".join(words)


def tokenize(line: str) -> Iterable[str]:
    # Simple whitespace split; in realistic cases, use regex
    return (w for w in line.strip().split() if w)


def benchmark(sc, rdd):
    # BASELINE: flatMap -> map -> reduceByKey
    t0 = time.perf_counter()
    base_counts = (rdd.flatMap(tokenize)
                   .map(lambda w: (w, 1))
                   .reduceByKey(add))
    base_total_unique = base_counts.count()  # action
    t1 = time.perf_counter()

    # MAP-SIDE AGG: flatMap -> mapPartitions(local dict) -> reduceByKey
    def partition_count(iter_words: Iterator[str]) -> Iterator[Tuple[str, int]]:
        d = {}
        for w in iter_words:
            d[w] = d.get(w, 0) + 1
        return d.items()

    t2 = time.perf_counter()
    ms_counts = (rdd.flatMap(tokenize)
                 .mapPartitions(partition_count)
                 .reduceByKey(add))
    ms_total_unique = ms_counts.count()  # action
    t3 = time.perf_counter()

    return {
        "baseline_secs": t1 - t0,
        "mapside_secs": t3 - t2,
        "baseline_unique": base_total_unique,
        "mapside_unique": ms_total_unique,
    }


def main():
    args = parse_args()

    builder = (SparkSession.builder.appName("benchmark-mapside-vs-baseline")
               .config("spark.sql.adaptive.enabled", "true")
               .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
               .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", 134217728)
               .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
               .config("spark.sql.shuffle.partitions", max(8, args.partitions)))

    if args.master:
        builder = builder.master(args.master)

    spark = builder.getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel("WARN")

    # Synthetic skewed dataset
    zipf_weights = make_zipf_weights(args.vocab, args.zipf)

    # Create a seed RDD of partition indices to generate data on executors
    seed_rdd = sc.parallelize(range(args.partitions), args.partitions)

    rdd = seed_rdd.mapPartitionsWithIndex(
        lambda idx, iter: gen_lines_in_partition(
            idx, args.records, args.partitions, args.avg_words, args.vocab, zipf_weights, args.seed)
    )

    print(f"=== Dataset ===")
    print(f"records={args.records}, avg_words={args.avg_words}, partitions={args.partitions}, "
          f"vocab={args.vocab}, zipf={args.zipf}")
    est_tokens = args.records * args.avg_words
    print(f"estimated total tokens ~ {est_tokens:,}")

    results = benchmark(sc, rdd)

    print("\n=== Results (wall clock) ===")
    print(f"Baseline (flatMap -> map -> reduceByKey): {results['baseline_secs']:.3f} sec")
    print(f"Map-side (flatMap -> mapPartitions -> reduceByKey): {results['mapside_secs']:.3f} sec")
    speedup = results['baseline_secs'] / results['mapside_secs'] if results['mapside_secs'] > 0 else float('inf')
    print(f"Speedup: {speedup:.2f}x")

    # Sanity check: unique word counts should match
    ok = results['baseline_unique'] == results['mapside_unique']
    print("\n=== Sanity ===")
    print(f"Unique words match: {ok} (baseline={results['baseline_unique']}, mapside={results['mapside_unique']})")

    print("\nTip: Open Spark UI at http://localhost:4040 and compare Shuffle Read/Write for the two jobs/stages.")
    print("      Map-side aggregation should reduce shuffle write volume when keys repeat within partitions.")


    input("Job complete. Press Enter to stop Spark and close UI...")

    spark.stop()


if __name__ == "__main__":
    main()