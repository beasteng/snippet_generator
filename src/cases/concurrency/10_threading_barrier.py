"""10 — Barrier for synchronization point.
INTERVIEW TIP: All threads block at barrier.wait() until the
required number have arrived, then all proceed together.
Useful for phased computation.
"""
import threading

barrier = threading.Barrier(3)

def worker(i):
    print(f"Worker {i} before barrier")
    barrier.wait()
    print(f"Worker {i} after barrier")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
