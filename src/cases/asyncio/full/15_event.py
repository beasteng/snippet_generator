"""#15 — asyncio.Event: one-shot signal between coroutines."""
import asyncio


async def waiter(event: asyncio.Event, name: str):
    print(f"  [{name}] waiting for event...")
    await event.wait()
    print(f"  [{name}] event fired! Proceeding.")


async def setter(event: asyncio.Event):
    print("  [setter] doing setup work...")
    await asyncio.sleep(2)
    print("  [setter] firing event!")
    event.set()


async def main():
    event = asyncio.Event()
    await asyncio.gather(
        waiter(event, "A"),
        waiter(event, "B"),
        waiter(event, "C"),
        setter(event),
    )


if __name__ == "__main__":
    asyncio.run(main())
