"""30 — asyncio.Queue producer-consumer pattern.
INTERVIEW TIP: This is the async equivalent of the
threading producer-consumer pattern (#08).
TaskGroup (3.11+) or gather() can run producers and consumers
concurrently.  task_done() + join() enable graceful shutdown.
"""
import asyncio
import random

async def producer(queue: asyncio.Queue, name: str):
    for i in range(5):
        await asyncio.sleep(random.uniform(0.05, 0.2))
        item = f"{name}-{i}"
        await queue.put(item)
        print(f"  [{name}] produced {item}")
    await queue.put(None)  # sentinel

async def consumer(queue: asyncio.Queue, name: str):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        print(f"  [{name}] consumed {item}")
        await asyncio.sleep(random.uniform(0.05, 0.15))
        queue.task_done()

async def main():
    q: asyncio.Queue = asyncio.Queue(maxsize=5)
    # Run 2 producers and 2 consumers concurrently
    await asyncio.gather(
        producer(q, "P1"),
        producer(q, "P2"),
        consumer(q, "C1"),
        consumer(q, "C2"),
    )
    print("All done!")

asyncio.run(main())
