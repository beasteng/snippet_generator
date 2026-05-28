"""#12 — Async Iterator: use 'async for' to consume data that arrives over time."""
import asyncio


class PaginatedAPI:
    """Simulates an API that returns pages of data."""

    def __init__(self, total_pages: int):
        self._total = total_pages
        self._page = 0

    def __aiter__(self):
        return self

    async def __anext__(self) -> list[int]:
        if self._page >= self._total:
            raise StopAsyncIteration
        self._page += 1
        await asyncio.sleep(0.5)
        return [self._page * 10 + i for i in range(3)]


async def main():
    api = PaginatedAPI(total_pages=4)
    async for page_data in api:
        print(f"  Page data: {page_data}")


if __name__ == "__main__":
    asyncio.run(main())
