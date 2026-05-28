"""#9 — Semaphore: limit concurrent access (rate-limiting, pool size)."""
import asyncio


async def download(url: str, sem: asyncio.Semaphore):
    async with sem:
        print(f"  ⬇ downloading {url}")
        await asyncio.sleep(1)
        print(f"  ✅ finished   {url}")
        return f"data-from-{url}"


async def main():
    sem = asyncio.Semaphore(3)
    urls = [f"https://api.example.com/page/{i}" for i in range(8)]
    results = await asyncio.gather(*(download(u, sem) for u in urls))
    print(f"\nCollected {len(results)} results")


if __name__ == "__main__":
    asyncio.run(main())
