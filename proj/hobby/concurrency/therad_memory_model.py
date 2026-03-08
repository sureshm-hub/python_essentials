import threading
import time

shared_data = []

def append_items(items: list) -> None:
    for item in items:
        shared_data.append(item)  # Directly modifies shared list
        time.sleep(0.001)

threads = [
    threading.Thread(target=append_items, args=([1, 2, 3],)),
    threading.Thread(target=append_items, args=([4, 5, 6],)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"result after thread process {shared_data}")  # Contains items from both threads


import multiprocessing

shared_data = []  # This is NOT actually shared!

def append_items(items: list) -> None:
    for item in items:
        shared_data.append(item)
    print(f"Process sees: {shared_data}")