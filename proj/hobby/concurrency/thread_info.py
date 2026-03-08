import threading

def work():
    print("busy working")

thread = threading.Thread(target=work, name="Worker")

# Before start
print(thread.is_alive())  # False
print(thread.ident)       # None
print(thread.name)        # Worker

thread.start()

# During execution
print(thread.is_alive())  # True
print(thread.ident)       # OS thread ID (int)

thread.join()

# After completion
print(thread.is_alive())  # False
print(thread.ident)       # Still has the ID from when it ran


# Get current thread
current = threading.current_thread()
print(f"Current thread: {current.name}")

# Get main thread
main = threading.main_thread()
print(f"Main thread: {main.name}")

# List all active threads
for t in threading.enumerate():
    print(f"Active: {t.name}, daemon={t.daemon}")

# Count active threads
print(f"Active count: {threading.active_count()}")