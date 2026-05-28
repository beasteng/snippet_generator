"""#6 — to_thread: offload blocking I/O without freezing the loop (3.9+)."""
import asyncio
import time


def cpu_heavy(n: int) -> int:
    """Simulates blocking work (never do this directly in async code)."""
    time.sleep(2)
    return n * n


async def main():
    a, b = await asyncio.gather(
        asyncio.to_thread(cpu_heavy, 5),
        asyncio.to_thread(cpu_heavy, 10),
    )
    print(f"Results: {a}, {b}")


if __name__ == "__main__":
    asyncio.run(main())
