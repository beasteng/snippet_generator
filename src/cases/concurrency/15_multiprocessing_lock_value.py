"""15 — Shared Value with Lock.
INTERVIEW TIP: Value and Array live in shared memory.
You MUST use a Lock to prevent race conditions.
"""
from multiprocessing import Process, Lock, Value

def increment(counter, lock):
    for _ in range(100_000):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    counter = Value("i", 0)
    lock = Lock()
    ps = [Process(target=increment, args=(counter, lock)) for _ in range(4)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    print(f"Counter = {counter.value}")  # 400000
