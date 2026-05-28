"""#28 — Async retry decorator with exponential backoff: production pattern."""
import asyncio
import functools
import random


def async_retry(max_retries: int = 3, base_delay: float = 1.0, backoff: float = 2.0):
    """Decorator: retries async functions with exponential backoff + jitter."""

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            delay = base_delay
            last_exc = None
            for attempt in range(1, max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    jitter = random.uniform(0, delay * 0.5)
                    wait = delay + jitter
                    print(
                        f"  [retry] attempt {attempt}/{max_retries} "
                        f"failed: {e!r}, retrying in {wait:.2f}s"
                    )
                    await asyncio.sleep(wait)
                    delay *= backoff
            raise last_exc

        return wrapper

    return decorator


call_count = 0


@async_retry(max_retries=5, base_delay=0.5, backoff=2.0)
async def flaky_api_call() -> str:
    global call_count
    call_count += 1
    if call_count < 4:
        raise ConnectionError(f"attempt {call_count} — server unavailable")
    return "success!"


async def main():
    try:
        result = await flaky_api_call()
        print(f"  Final result: {result}")
    except ConnectionError as e:
        print(f"  All retries exhausted: {e}")


if __name__ == "__main__":
    asyncio.run(main())
