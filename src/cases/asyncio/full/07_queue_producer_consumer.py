"""#7 — asyncio.Queue: producer/consumer with backpressure."""
import asyncio
import random


async def producer(q: asyncio.Queue, pid: int, count: int):
    for i in range(count):
        item = f"P{pid}-item{i}"
        await q.put(item)
        print(f"  [producer-{pid}] put {item}")
        await asyncio.sleep(random.uniform(0.1, 0.3))
    await q.put(None)


async def consumer(q: asyncio.Queue, cid: int, total_producers: int):
    done_count = 0
    while done_count < total_producers:
        item = await q.get()
        if item is None:
            done_count += 1
            continue
        print(f"  [consumer-{cid}] processing {item}")
        await asyncio.sleep(0.2)
        q.task_done()


async def main():
    q: asyncio.Queue = asyncio.Queue(maxsize=3)
    producers = [producer(q, i, 4) for i in range(2)]
    consumers = [consumer(q, 0, total_producers=2)]
    await asyncio.gather(*producers, *consumers)
    print("Pipeline finished.")


if __name__ == "__main__":
    asyncio.run(main())
