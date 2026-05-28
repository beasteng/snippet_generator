"""24 — Exception handling with Futures.
INTERVIEW TIP: Exceptions raised inside a Future are re-raised
when you call .result().  Use try/except around .result().
"""
from concurrent.futures import ThreadPoolExecutor, as_completed

def risky(x):
    if x == 3:
        raise ValueError(f"Bad value: {x}")
    return x * 10

with ThreadPoolExecutor() as ex:
    futures = [ex.submit(risky, i) for i in range(5)]
    for f in as_completed(futures):
        try:
            print(f.result())
        except ValueError as e:
            print(f"Caught: {e}")
