"""05 — Lock for thread-safe counter.
INTERVIEW TIP: Without the lock, += is NOT atomic in CPython
(it's LOAD, ADD, STORE bytecodes).  Always protect shared
mutable state with a Lock.
"""
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:          # context manager = acquire + release
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter = {counter}")   # always 400000
