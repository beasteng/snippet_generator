"""07 — Event for signaling between threads.
INTERVIEW TIP: Event is a simple flag.  One thread waits,
another sets it.  Great for start signals or shutdown flags.
"""
import threading
import time

ready = threading.Event()

def waiter():
    print("Waiting for signal...")
    ready.wait()            # blocks until set()
    print("Got signal! Proceeding.")

t = threading.Thread(target=waiter)
t.start()
time.sleep(1)
ready.set()                 # unblocks the waiter
t.join()
