"""#3 — gather: run many coroutines, results always in input order."""
import asyncio


async def fetch(n: int) -> dict:
    await asyncio.sleep(n)
    return {"task": n, "status": "ok"}


async def main():
    results = await asyncio.gather(fetch(3), fetch(1), fetch(2))
    for r in results:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
