"""28 — asyncio.gather for concurrent coroutines.
INTERVIEW TIP: gather() runs multiple awaitables concurrently
and returns results in the SAME order.  It's the asyncio
equivalent of Promise.all().
"""
import asyncio

async def fetch(i):
    await asyncio.sleep(0.1 * i)
    return f"result-{i}"

async def main():
    results = await asyncio.gather(*(fetch(i) for i in range(5)))
    print(results)

asyncio.run(main())
