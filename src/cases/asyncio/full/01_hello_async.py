"""#1 — Basic async/await: the building block of everything."""
import asyncio


async def greet(name: str) -> str:
    print(f"Hello, {name}! (about to sleep)")
    await asyncio.sleep(1)
    return f"Goodbye, {name}!"


async def main():
    result = await greet("World")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
