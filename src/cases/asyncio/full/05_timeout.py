"""#5 — wait_for timeout: cancel slow work automatically."""
import asyncio


async def slow_api_call() -> str:
    await asyncio.sleep(10)
    return "data"


async def main():
    try:
        result = await asyncio.wait_for(slow_api_call(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("API call timed out after 2s — task was cancelled")


if __name__ == "__main__":
    asyncio.run(main())
