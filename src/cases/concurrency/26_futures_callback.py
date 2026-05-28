"""26 — Adding callbacks to Futures.
INTERVIEW TIP: add_done_callback(fn) is called when the future
completes (success or exception).  Runs in the executor's thread.
"""
from concurrent.futures import ThreadPoolExecutor
import time

def task(x):
    time.sleep(0.5)
    return x * x

def on_done(future):
    print(f"Callback: result = {future.result()}")

with ThreadPoolExecutor() as ex:
    f = ex.submit(task, 7)
    f.add_done_callback(on_done)
    # main thread can do other work here
    time.sleep(1)
