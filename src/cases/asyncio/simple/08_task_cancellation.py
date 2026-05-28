"""Task cancellation — graceful cleanup on cancel."""
import asyncio


async def worker():
    try:
        while True:
            print("working...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("cleanup after cancel")
        raise  # Always re-raise!


async def main():
    task = asyncio.create_task(worker())
    await asyncio.sleep(2.5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("task was cancelled")


if __name__ == "__main__":
    asyncio.run(main())
