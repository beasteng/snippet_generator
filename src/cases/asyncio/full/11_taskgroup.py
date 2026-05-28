"""#11 — TaskGroup: structured concurrency (Python 3.11+).
   Auto-cancels siblings on failure. Replaces gather in modern code."""
import asyncio


async def job(n: int) -> int:
    await asyncio.sleep(n)
    return n * 10


async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(job(1))
        t2 = tg.create_task(job(2))
        t3 = tg.create_task(job(3))
    print(f"Results: {t1.result()}, {t2.result()}, {t3.result()}")


if __name__ == "__main__":
    asyncio.run(main())
