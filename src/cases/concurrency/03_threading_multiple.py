"""03 — Spawning multiple threads and joining all.
INTERVIEW TIP: Always join ALL threads to prevent the main
process from exiting prematurely.
"""
import threading

def worker(i):
    print(f"Worker {i} running")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("All workers done")
