"""#2 — create_task: schedule coroutines to run concurrently."""
import asyncio
import time


async def job(name: str, seconds: int) -> str:
    await asyncio.sleep(seconds)
    return f"{name} done"


async def main():
    start = time.perf_counter()

    t1 = asyncio.create_task(job("A", 1))
    t2 = asyncio.create_task(job("B", 2))
    t3 = asyncio.create_task(job("C", 1))

    print(await t1, "|", await t2, "|", await t3)
    print(f"Elapsed: {time.perf_counter() - start:.1f}s")


if __name__ == "__main__":
    asyncio.run(main())
