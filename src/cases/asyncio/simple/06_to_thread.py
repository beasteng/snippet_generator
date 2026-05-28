"""Run blocking/sync code with to_thread (Python 3.9+)."""
import asyncio
import time


def blocking_io() -> str:
    """Simulates a slow synchronous I/O operation."""
    time.sleep(2)
    return "blocking done"


async def main():
    print("Starting blocking call in a thread...")
    result = await asyncio.to_thread(blocking_io)
    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
