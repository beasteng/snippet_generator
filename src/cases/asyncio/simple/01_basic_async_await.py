"""Basic async/await — the foundation of asyncio."""
import asyncio


async def fetch():
    await asyncio.sleep(1)
    return "done"


async def main():
    result = await fetch()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
