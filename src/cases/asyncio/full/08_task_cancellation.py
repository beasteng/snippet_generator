"""#8 — Task cancellation with proper cleanup."""
import asyncio


async def heartbeat():
    try:
        while True:
            print("  ♥ heartbeat")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("  ♥ heartbeat cleanup")
        raise


async def main():
    task = asyncio.create_task(heartbeat())
    await asyncio.sleep(3.5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Heartbeat stopped cleanly.")


if __name__ == "__main__":
    asyncio.run(main())
