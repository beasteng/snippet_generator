"""#13 — Async Generator: yield values asynchronously."""
import asyncio


async def ticker(label: str, count: int, delay: float):
    """Yields tick events at given intervals."""
    for i in range(count):
        await asyncio.sleep(delay)
        yield f"{label}-tick-{i}"


async def main():
    async for tick in ticker("sensor", 5, 0.5):
        print(f"  Received: {tick}")

    data = [t async for t in ticker("batch", 3, 0.2)]
    print(f"  Collected: {data}")


if __name__ == "__main__":
    asyncio.run(main())
