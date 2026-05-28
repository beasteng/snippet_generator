"""#19 — asyncio.wait with FIRST_COMPLETED: react to the fastest result."""
import asyncio
import random


async def query_replica(name: str) -> str:
    delay = random.uniform(0.5, 3.0)
    await asyncio.sleep(delay)
    return f"{name} responded in {delay:.2f}s"


async def main():
    tasks = {
        asyncio.create_task(query_replica(f"replica-{i}"))
        for i in range(5)
    }

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    winner = done.pop()
    print(f"  Winner: {winner.result()}")

    for t in pending:
        t.cancel()
    print(f"  Cancelled {len(pending)} slower tasks")


if __name__ == "__main__":
    asyncio.run(main())
