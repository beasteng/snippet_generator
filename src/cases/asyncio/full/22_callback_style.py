"""#22 — Low-level callbacks + Futures: understand what's beneath async/await."""
import asyncio


def old_style_callback(future: asyncio.Future):
    """Callbacks were the pre-await way to handle async results."""
    print(f"  [callback] result = {future.result()}")


async def main():
    loop = asyncio.get_running_loop()

    fut: asyncio.Future = loop.create_future()
    fut.add_done_callback(old_style_callback)

    loop.call_later(1.0, fut.set_result, "hello from future")
    await fut

    print("\n  Scheduling callbacks:")
    loop.call_soon(lambda: print("  [call_soon] fires ASAP"))
    loop.call_later(0.5, lambda: print("  [call_later] fires in 0.5s"))
    await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
