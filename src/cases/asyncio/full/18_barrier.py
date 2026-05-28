"""#18 — asyncio.Barrier: synchronize N tasks at a rendezvous point (3.11+)."""
import asyncio


async def worker(barrier: asyncio.Barrier, wid: int):
    print(f"  [worker-{wid}] doing setup...")
    await asyncio.sleep(wid * 0.5)
    print(f"  [worker-{wid}] waiting at barrier")
    await barrier.wait()
    print(f"  [worker-{wid}] passed barrier — starting phase 2")


async def main():
    barrier = asyncio.Barrier(3)
    await asyncio.gather(worker(barrier, 1), worker(barrier, 2), worker(barrier, 3))


if __name__ == "__main__":
    asyncio.run(main())
