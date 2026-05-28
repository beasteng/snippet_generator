"""#10 — Real async HTTP with aiohttp + semaphore rate-limiting."""
import asyncio

try:
    import aiohttp
except ImportError:
    raise SystemExit("pip install aiohttp")


async def fetch(session: aiohttp.ClientSession, url: str, sem: asyncio.Semaphore):
    async with sem:
        async with session.get(url) as resp:
            data = await resp.text()
            return {"url": url, "status": resp.status, "length": len(data)}


async def main():
    sem = asyncio.Semaphore(5)
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts/1",
    ]
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *(fetch(session, u, sem) for u in urls),
            return_exceptions=True,
        )
    for r in results:
        print(f"  {r}")


if __name__ == "__main__":
    asyncio.run(main())
