"""
08 — Retry with Exponential Backoff
=====================================
Wrap flaky LLM/tool calls with retries.
Interview point: Production agents MUST handle transient failures.
"""
import time
import random
from typing import TypeVar, Callable

T = TypeVar("T")

def retry(fn: Callable[..., T], max_attempts: int = 3,
          base_delay: float = 0.5) -> T:
    for attempt in range(1, max_attempts + 1):
        try:
            return fn()
        except Exception as e:
            if attempt == max_attempts:
                raise
            delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 0.1)
            print(f"  Attempt {attempt} failed ({e}), retrying in {delay:.2f}s")
            time.sleep(delay)

# Simulate a flaky API
call_count = 0
def flaky_api():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("server busy")
    return "success on attempt 3"

if __name__ == "__main__":
    result = retry(flaky_api)
    print("Result:", result)
