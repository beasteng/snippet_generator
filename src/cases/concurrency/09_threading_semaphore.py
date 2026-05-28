"""09 — Semaphore to limit concurrency.
INTERVIEW TIP: Semaphore(n) allows at most n threads to enter
the critical section simultaneously.  Perfect for rate-limiting
or connection pool patterns.
"""
import threading
import time

sem = threading.Semaphore(2)    # max 2 concurrent

def task(i):
    with sem:
        print(f"Start {i}")
        time.sleep(0.5)
        print(f"End   {i}")

threads = [threading.Thread(target=task, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
