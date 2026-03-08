import multiprocessing
import time

def cpu_bound_task(n: int) -> int:
    count = 0
    for i in range(n):
        count += i
    return count

def run_multiprocess(task, iterations: int, num_tasks: int) -> float:
    start = time.perf_counter()

    with multiprocessing.Pool(processes=num_tasks) as pool:
        # Runs task(10_000_000) 4 times in parallel
        # map() blocks until all tasks are complete and returns the results
        # automatically manages a fixed pool of worker processes, distributing tasks to idle workers without manual
        # intervention
        result = pool.map(task, [iterations] * num_tasks)
    print("All Process Finished.", end="\n")
    print(f"results in order of execution: {result}")
    return time.perf_counter() - start

if __name__ == "__main__":
    ITERATIONS = 10_000_000
    NUM_TASKS = 4

    mp_time = run_multiprocess(cpu_bound_task, ITERATIONS, NUM_TASKS)
    print(f"Multiprocessing: {mp_time:.2f}s")