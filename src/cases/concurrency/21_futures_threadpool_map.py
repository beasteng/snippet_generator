"""21 — ThreadPoolExecutor.map (high-level API).
INTERVIEW TIP: concurrent.futures is the *recommended* high-level
interface.  Executor.map preserves input order.
"""
from concurrent.futures import ThreadPoolExecutor

def double(x):
    return x * 2

with ThreadPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(double, range(10))))
