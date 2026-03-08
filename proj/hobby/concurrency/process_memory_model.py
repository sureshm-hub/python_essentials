import multiprocessing

shared_data = []  # This is NOT actually shared!

def append_items(items: list) -> None:
    for item in items:
        shared_data.append(item)
    print(f"Process sees: {shared_data}")

if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=append_items, args=([1, 2, 3],)),
        multiprocessing.Process(target=append_items, args=([4, 5, 6],)),
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Main sees: {shared_data}")  # Empty!