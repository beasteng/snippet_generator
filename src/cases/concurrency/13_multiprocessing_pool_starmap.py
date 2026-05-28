"""13 — Pool.starmap for multi-argument functions.
INTERVIEW TIP: starmap unpacks each tuple as *args.
"""
from multiprocessing import Pool

def add(a, b):
    return a + b

if __name__ == "__main__":
    with Pool() as pool:
        results = pool.starmap(add, [(1, 2), (3, 4), (5, 6)])
    print(results)  # [3, 7, 11]
