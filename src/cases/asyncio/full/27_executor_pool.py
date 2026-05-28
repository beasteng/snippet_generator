"""#27 — Custom executor pools: ProcessPool for CPU, ThreadPool for I/O."""
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import math
import time


def cpu_bound(n: int) -> float:
    """Heavy computation — must run in a process pool."""
    return sum(math.sin(i) for i in range(n))


def io_bound(seconds: float) -> str:
    """Blocking I/O — thread pool is fine."""
    time.sleep(seconds)
    return f"slept {seconds}s"


async def main():
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor(max_workers=4) as proc_pool:
        futures = [
            loop.run_in_executor(proc_pool, cpu_bound, 5_000_000)
            for _ in range(4)
        ]
        results = await asyncio.gather(*futures)
        print(f"  CPU results: {[f'{r:.2f}' for r in results]}")

    with ThreadPoolExecutor(max_workers=4) as thread_pool:
        futures = [
            loop.run_in_executor(thread_pool, io_bound, 0.5)
            for _ in range(4)
        ]
        results = await asyncio.gather(*futures)
        print(f"  I/O results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
