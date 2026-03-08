import threading
import time

def do_work(id,  priority = 1):
    print(f"work {id} started with priority {priority}\n")

# target based thread
demo_thread = threading.Thread(
    target = do_work,
    args = (1001,), # positional args as tuple
    kwargs={'priority': 5}, # kwargs as dict
    name = "demo_thread"
)

demo_thread.start()
print(demo_thread.native_id) # matches with top or ps.
print(demo_thread.ident) # OS-assigned integer


# Lambda with captured variables
multiplier = 10
thread = threading.Thread(
    target=lambda: print(f"Result: {5 * multiplier}")
)
thread.start()

# Subclass
class DownloadThread(threading.Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.result = None

    def run(self):
        time.sleep(1)
        # Simulated download
        self.result = f"Downloaded: {self.url}"

thread = DownloadThread("https://example.com/data")
thread.start()
thread.join()
print(thread.result)

# callable
class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.result = None

    def __call__(self):
        print(f"Processing {len(self.data)} items")
        self.result = [x * 2 for x in self.data]

# Usage
processor = DataProcessor([1, 2, 3, 4, 5])
thread = threading.Thread(target=processor, name="DataProcessor")
thread.start()
thread.join()
print(processor.result)  # [2, 4, 6, 8, 10]