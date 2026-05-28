"""#26 — Debug mode + slow callback detection: find async anti-patterns."""
import asyncio
import time
import logging


async def accidental_blocking():
    """BAD: blocking call in async code — debug mode will warn!"""
    time.sleep(0.2)


async def good_coroutine():
    await asyncio.sleep(0.1)


async def main():
    loop = asyncio.get_running_loop()

    loop.slow_callback_duration = 0.1

    print(f"  Debug mode: {loop.get_debug()}")
    print(f"  Slow callback threshold: {loop.slow_callback_duration}s")

    await good_coroutine()
    await accidental_blocking()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)
