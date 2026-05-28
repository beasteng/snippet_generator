"""#29 — Fan-out / Fan-in pipeline: distribute work, collect results."""
import asyncio
import random


async def fetch_urls(urls: list[str], raw_queue: asyncio.Queue):
    """Fan-out: fetch all URLs concurrently, push raw data to queue."""
    async def _fetch(url: str):
        await asyncio.sleep(random.uniform(0.2, 1.0))
        data = f"data-from-{url}"
        await raw_queue.put(data)

    await asyncio.gather(*[_fetch(u) for u in urls])
    await raw_queue.put(None)


async def transform(raw_queue: asyncio.Queue, result_queue: asyncio.Queue):
    """Middle stage: transform each item."""
    while True:
        item = await raw_queue.get()
        if item is None:
            await result_queue.put(None)
            break
        transformed = item.upper()
        await asyncio.sleep(0.1)
        await result_queue.put(transformed)


async def collect(result_queue: asyncio.Queue) -> list[str]:
    """Fan-in: collect all transformed results."""
    results = []
    while True:
        item = await result_queue.get()
        if item is None:
            break
        results.append(item)
    return results


async def main():
    raw_q: asyncio.Queue = asyncio.Queue()
    result_q: asyncio.Queue = asyncio.Queue()

    urls = [f"page-{i}" for i in range(6)]

    fetcher = asyncio.create_task(fetch_urls(urls, raw_q))
    transformer = asyncio.create_task(transform(raw_q, result_q))
    collector = asyncio.create_task(collect(result_q))

    await fetcher
    await transformer
    results = await collector
    print(f"  Pipeline output ({len(results)} items):")
    for r in results:
        print(f"    {r}")


if __name__ == "__main__":
    asyncio.run(main())
