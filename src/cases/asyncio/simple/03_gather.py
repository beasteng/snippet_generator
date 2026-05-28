"""gather — run many coroutines and collect results in input order."""
import asyncio


async def job(n: int) -> int:
    await asyncio.sleep(n)
    return n


async def main():
    results = await asyncio.gather(job(1), job(2), job(3))
    print(f"Results (always in order): {results}")


if __name__ == "__main__":
    asyncio.run(main())
