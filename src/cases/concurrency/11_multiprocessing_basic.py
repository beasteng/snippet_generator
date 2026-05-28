"""11 — Basic multiprocessing.
INTERVIEW TIP: Use multiprocessing for CPU-bound work.
Each Process runs in its own interpreter — bypasses the GIL.
"""
from multiprocessing import Process

def worker():
    print("Hello from child process")

if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    p.join()
