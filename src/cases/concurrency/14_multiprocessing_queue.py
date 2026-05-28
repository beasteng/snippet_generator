"""14 — Inter-process communication with Queue.
INTERVIEW TIP: multiprocessing.Queue uses pipes + locks under
the hood.  It's the MP equivalent of queue.Queue for threads.
"""
from multiprocessing import Process, Queue

def producer(q):
    for i in range(5):
        q.put(i)

def consumer(q):
    while not q.empty():
        print("Got", q.get())

if __name__ == "__main__":
    q = Queue()
    p = Process(target=producer, args=(q,))
    p.start()
    p.join()
    c = Process(target=consumer, args=(q,))
    c.start()
    c.join()
