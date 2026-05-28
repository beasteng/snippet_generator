"""Concurrent execution with create_task — tasks run concurrently."""
import asyncio


async def job(n: int) -> int:
    await asyncio.sleep(n)
    return n


async def main():
    t1 = asyncio.create_task(job(1))
    t2 = asyncio.create_task(job(2))
    # Both run concurrently — total time ≈ 2s, not 3s
    r1, r2 = await t1, await t2
    print(f"Results: {r1}, {r2}")


if __name__ == "__main__":
    asyncio.run(main())
