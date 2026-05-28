"""01 — Basic thread creation and joining.
INTERVIEW TIP: threading.Thread is the simplest way to run code
concurrently.  .join() blocks until the thread finishes.
Good for I/O-bound work; the GIL prevents true CPU parallelism.
"""
import threading

def worker():
    print("Hello from thread")

t = threading.Thread(target=worker)
t.start()
t.join()  # wait for thread to finish
print("Main thread done")
