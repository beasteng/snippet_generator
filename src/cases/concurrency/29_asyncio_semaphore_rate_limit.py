"""29 — asyncio.Semaphore for rate limiting.
INTERVIEW TIP: Limit concurrent API calls / DB connections.
Same concept as threading.Semaphore but for coroutines.
"""
import asyncio

sem = asyncio.Semaphore(2)

async def fetch(i):
    async with sem:
        print(f"Start {i}")
        await asyncio.sleep(0.5)
        print(f"End   {i}")
        return i

async def main():
    results = await asyncio.gather(*(fetch(i) for i in range(5)))
    print("Results:", results)

asyncio.run(main())
