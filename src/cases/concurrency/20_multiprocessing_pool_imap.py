"""20 — Pool.imap_unordered for streaming results.
INTERVIEW TIP: imap_unordered yields results as they finish
(not in input order).  Great for progress bars or early stopping.
"""
from multiprocessing import Pool
import time

def heavy(x):
    time.sleep(0.3 - x * 0.05)     # earlier items take longer
    return x * x

if __name__ == "__main__":
    with Pool(4) as pool:
        for result in pool.imap_unordered(heavy, range(6)):
            print(f"Got {result}")
