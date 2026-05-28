"""08 — Producer-Consumer with queue.Queue.
INTERVIEW TIP: queue.Queue is thread-safe by design.
Use a sentinel (None) to signal the consumer to stop.
This is the #1 pattern for inter-thread communication.
"""
import threading
from queue import Queue

q: Queue = Queue(maxsize=10)

def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced {i}")
    q.put(None)             # sentinel

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")

threading.Thread(target=producer).start()
c = threading.Thread(target=consumer)
c.start()
c.join()
