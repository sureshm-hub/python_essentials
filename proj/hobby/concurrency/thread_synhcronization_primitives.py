import threading
import time
import random

# Lock
lock = threading.Lock()
with lock:
    # Critical section - only one thread at a time
    print("entered lock", end="\n")
    pass

# Reentrant Lock
rlock = threading.RLock()
with rlock:
    with rlock:  # Same thread can acquire again without deadlock
        print("entered reentrant lock", end="\n")
        pass

# Event
event = threading.Event()
print("created threading event, set event notification (this happens across 2 different threads)", end="\n")
event.set()      # Signal that something happened
event.wait()     # Block until the event is set
event.clear()    # Reset for reuse

# Semaphore
semaphore = threading.Semaphore(3)  # Allow up to 3 concurrent threads
with semaphore:
    # At most 3 threads can be here simultaneously
    pass

# Condition Example
condition = threading.Condition()
with condition:
    print("entered condition, waiting to be notified", end="\n")
    condition.notify()  # Wake one waiting thread
    # following line of code needs a notification from a different thread
    # condition.wait()    # Release lock and wait for notification

# Condition Example for Producer, Consumer Scenario
# Shared data and the condition object
buffer = []
# A Condition object manages an underlying Lock
condition = threading.Condition()

def consumer():
    with condition:
        while not buffer:
            print("Consumer: Waiting for items...")
            condition.wait()  # Releases lock and waits for notify()
        # Once notified, it re-acquires the lock automatically
        item = buffer.pop()
        print(f"Consumer: Consumed {item}")

def producer():
    time.sleep(2)  # Simulate some work
    with condition:
        buffer.append("Product")
        print("Producer: Produced item. Notifying consumer...")
        condition.notify()  # Signal one waiting thread to wake up

# Setup and run threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()