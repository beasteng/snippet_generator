"""Timeouts with wait_for — cancel a coroutine if it takes too long."""
import asyncio


async def slow():
    await asyncio.sleep(5)
    return "finished"


async def main():
    try:
        result = await asyncio.wait_for(slow(), timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print("Timed out! The coroutine took longer than 1 second.")


if __name__ == "__main__":
    asyncio.run(main())
