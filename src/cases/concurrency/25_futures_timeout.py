"""25 — Future timeout.
INTERVIEW TIP: .result(timeout=N) raises TimeoutError if the
task hasn't finished in N seconds.  The task keeps running though!
"""
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import time

def slow():
    time.sleep(3)
    return "done"

with ThreadPoolExecutor() as ex:
    f = ex.submit(slow)
    try:
        print(f.result(timeout=1))
    except TimeoutError:
        print("Timed out! (task still running in background)")
