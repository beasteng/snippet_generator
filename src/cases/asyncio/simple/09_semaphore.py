"""Limit concurrency with Semaphore — e.g. rate-limiting API calls."""
import asyncio


async def task(n: int, sem: asyncio.Semaphore):
    async with sem:
        print(f"  start task {n}")
        await asyncio.sleep(1)
        print(f"  end   task {n}")


async def main():
    sem = asyncio.Semaphore(2)  # Max 2 concurrent tasks
    await asyncio.gather(*(task(i, sem) for i in range(5)))
    print("All tasks finished.")


if __name__ == "__main__":
    asyncio.run(main())
