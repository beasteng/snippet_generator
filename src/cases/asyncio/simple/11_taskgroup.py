"""TaskGroup — structured concurrency (Python 3.11+)."""
import asyncio


async def job(n: int) -> int:
    await asyncio.sleep(n)
    print(f"  job({n}) finished")
    return n


async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(job(1))
        t2 = tg.create_task(job(2))
        t3 = tg.create_task(job(3))

    # All tasks guaranteed complete here
    print(f"Results: {t1.result()}, {t2.result()}, {t3.result()}")


if __name__ == "__main__":
    asyncio.run(main())
