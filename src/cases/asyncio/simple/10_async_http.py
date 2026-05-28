"""Async HTTP requests with aiohttp (pip install aiohttp)."""
import asyncio

try:
    import aiohttp
except ImportError:
    print("Install aiohttp first:  pip install aiohttp")
    raise SystemExit(1)


async def fetch(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as resp:
        body = await resp.text()
        return resp.status, len(body)


async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts/1",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, u) for u in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for url, result in zip(urls, results):
            if isinstance(result, Exception):
                print(f"  {url} -> ERROR: {result}")
            else:
                status, length = result
                print(f"  {url} -> status={status}, length={length}")


if __name__ == "__main__":
    asyncio.run(main())
