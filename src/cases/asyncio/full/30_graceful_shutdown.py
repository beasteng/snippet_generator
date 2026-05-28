"""#30 — Graceful shutdown: handle SIGINT/SIGTERM, cancel all tasks cleanly."""
import asyncio
import signal
import sys


async def background_worker(name: str):
    try:
        while True:
            print(f"  [{name}] working...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print(f"  [{name}] shutting down gracefully...")
        await asyncio.sleep(0.2)
        print(f"  [{name}] cleanup done")
        raise


async def shutdown(sig: signal.Signals, loop: asyncio.AbstractEventLoop):
    print(f"\n  Received signal {sig.name}. Shutting down...")
    tasks = [
        t for t in asyncio.all_tasks()
        if t is not asyncio.current_task()
    ]
    print(f"  Cancelling {len(tasks)} outstanding tasks")

    for task in tasks:
        task.cancel()

    results = await asyncio.gather(*tasks, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception) and not isinstance(r, asyncio.CancelledError):
            print(f"  ⚠ Task exception during shutdown: {r!r}")

    loop.stop()


async def main():
    loop = asyncio.get_running_loop()

    if sys.platform != "win32":
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(
                sig,
                lambda s=sig: asyncio.create_task(shutdown(s, loop)),
            )

    workers = [
        asyncio.create_task(background_worker(f"worker-{i}"))
        for i in range(3)
    ]

    print("  Press Ctrl+C to trigger graceful shutdown\n")

    try:
        await asyncio.gather(*workers)
    except asyncio.CancelledError:
        pass

    print("  ✅ Shutdown complete")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n  (KeyboardInterrupt caught at top level)")
