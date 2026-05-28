"""#20 — asyncio.as_completed: process results in completion order."""
import asyncio
import random


async def fetch(url: str) -> dict:
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)
    return {"url": url, "delay": round(delay, 2)}


async def main():
    urls = [f"https://api.example.com/{i}" for i in range(5)]
    coros = [fetch(u) for u in urls]

    print("Results in completion order:")
    for coro in asyncio.as_completed(coros):
        result = await coro
        print(f"  ✅ {result}")


if __name__ == "__main__":
    asyncio.run(main())
