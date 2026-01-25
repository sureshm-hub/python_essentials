from pyspark.sql import SparkSession, functions as F
from datetime import datetime

# using RDD API
spark = SparkSession.builder.appName("WordCount").master("local[*]").getOrCreate()
sc = spark.sparkContext

text_file = "/notes.md"
lines = sc.textFile(text_file)

# reduce by key - efficient
words = lines.flatMap(lambda line: line.split(" "))
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
output_dir = f"C:/Users/sures/IdeaProjects/PythonEssentials/out/run_ts={datetime.now():%Y-%m-%d_%H-%M-%S}"
word_counts.saveAsTextFile(output_dir)

# example code for group by - less efficient, for example
word_counts_groupby = words.map(lambda word: (word, 1)).groupByKey().mapValues(sum)
output_dir = f"C:/Users/sures/IdeaProjects/PythonEssentials/out/group_by_run_ts={datetime.now():%Y-%m-%d_%H-%M-%S}"
word_counts_groupby.saveAsTextFile(output_dir)

# map side partitions
def partition_count(iterable):
    counts = {}
    for word in iterable:
        counts[word] = counts.get(word, 0)+1
    return counts.items()

word_counts = words.mapPartitions(partition_count).reduceByKey(lambda a, b: a + b)
results = word_counts.collect()
for word, count in results:
    if word.startswith("f"):
        print(f"{word}: {count}")

# using dataframe API
df = spark.read.text(text_file) # column "value"
words = (df.select(F.explode(F.split(F.lower(F.col("value")), r"\W+")).alias("word"))
                  .where(F.col("word") != ""))

# skew safe salting
buckets = 16
words = words.withColumn("salt",F.floor(F.rand()*buckets))

counts = words.groupBy("word", "salt").count().orderBy(F.desc("count"))
counts.drop("salt").write.mode("overwrite").csv("C:/Users/sures/IdeaProjects/PythonEssentials/out/word_counts.csv", header=True)

sc.stop()