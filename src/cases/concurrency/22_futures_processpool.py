"""22 — ProcessPoolExecutor for CPU-bound work.
INTERVIEW TIP: Same API as ThreadPoolExecutor — just swap the class.
Uses multiprocessing under the hood.
"""
from concurrent.futures import ProcessPoolExecutor

def square(x):
    return x * x

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as ex:
        print(list(ex.map(square, range(10))))
