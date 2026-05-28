"""12 — Pool.map for parallel computation.
INTERVIEW TIP: Pool.map distributes items across worker
processes.  This is the simplest way to parallelise a
function over a list.
"""
from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(square, range(10))
    print(results)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
