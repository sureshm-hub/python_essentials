import asyncio
import time

async def fetch_data(delay: float, name: str) -> str:
    print(f"{name}: starting")
    await asyncio.sleep(delay)  # Non-blocking wait
    print(f"{name}: done")
    return f"Data from {name}"

async def main():
    start = time.perf_counter()

    # Run concurrently
    results = await asyncio.gather(
        fetch_data(1.0, "Task A"),
        fetch_data(1.0, "Task B"),
        fetch_data(1.0, "Task C"),
    )

    elapsed = time.perf_counter() - start
    print(f"Completed in {elapsed:.2f}s")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())