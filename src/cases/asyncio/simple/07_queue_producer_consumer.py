"""Producer / Consumer pattern with asyncio.Queue."""
import asyncio


async def producer(q: asyncio.Queue, n_items: int):
    for i in range(n_items):
        await asyncio.sleep(0.5)
        await q.put(i)
        print(f"  [producer] put {i}")
    await q.put(None)  # Sentinel to signal "done"


async def consumer(q: asyncio.Queue):
    while True:
        item = await q.get()
        if item is None:
            print("  [consumer] received stop signal")
            break
        print(f"  [consumer] got {item}")
        q.task_done()


async def main():
    q: asyncio.Queue = asyncio.Queue(maxsize=2)
    await asyncio.gather(producer(q, 5), consumer(q))
    print("All done.")


if __name__ == "__main__":
    asyncio.run(main())
