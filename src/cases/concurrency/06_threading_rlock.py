"""06 — RLock (reentrant lock).
INTERVIEW TIP: RLock can be acquired multiple times BY THE SAME
thread without deadlocking.  Useful when a locked function calls
another locked function.
"""
import threading

rlock = threading.RLock()

def outer():
    with rlock:
        print("outer acquired")
        inner()             # would DEADLOCK with a regular Lock

def inner():
    with rlock:
        print("inner acquired")

t = threading.Thread(target=outer)
t.start()
t.join()
