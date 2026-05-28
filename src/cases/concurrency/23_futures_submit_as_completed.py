"""23 — submit() + as_completed() for unordered results.
INTERVIEW TIP: submit() returns a Future.  as_completed() yields
futures in the order they FINISH, not the order submitted.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def task(x):
    time.sleep(0.1 * (5 - x))  # lower x takes longer
    return x

with ThreadPoolExecutor(max_workers=3) as ex:
    futures = {ex.submit(task, i): i for i in range(5)}
    for f in as_completed(futures):
        original_input = futures[f]
        print(f"Input {original_input} → Result {f.result()}")
