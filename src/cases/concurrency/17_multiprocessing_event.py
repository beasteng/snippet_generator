"""17 — Event across processes.
INTERVIEW TIP: Works the same as threading.Event but
across process boundaries (uses shared memory internally).
"""
from multiprocessing import Process, Event
import time

def waiter(evt):
    print("Child waiting...")
    evt.wait()
    print("Child proceeding!")

if __name__ == "__main__":
    event = Event()
    p = Process(target=waiter, args=(event,))
    p.start()
    time.sleep(1)
    event.set()
    p.join()
