"""#17 — asyncio.Condition: wait until a complex predicate is true."""
import asyncio


async def consumer(cond: asyncio.Condition, data: list):
    async with cond:
        await cond.wait_for(lambda: len(data) >= 3)
        print(f"  [consumer] got enough data: {data}")


async def producer(cond: asyncio.Condition, data: list):
    for i in range(5):
        await asyncio.sleep(0.5)
        async with cond:
            data.append(i)
            print(f"  [producer] appended {i}, total={len(data)}")
            cond.notify_all()


async def main():
    cond = asyncio.Condition()
    data: list[int] = []
    await asyncio.gather(consumer(cond, data), producer(cond, data))


if __name__ == "__main__":
    asyncio.run(main())
