"""#14 — Async Context Manager: acquire/release async resources cleanly."""
import asyncio
from contextlib import asynccontextmanager


class AsyncDBConnection:
    """Class-based async context manager."""

    async def __aenter__(self):
        print("  [db] connecting...")
        await asyncio.sleep(0.5)
        print("  [db] connected")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("  [db] closing connection...")
        await asyncio.sleep(0.2)
        print("  [db] closed")
        return False

    async def query(self, sql: str) -> str:
        await asyncio.sleep(0.3)
        return f"result of '{sql}'"


@asynccontextmanager
async def managed_resource(name: str):
    """Decorator-based async context manager."""
    print(f"  Acquiring {name}")
    await asyncio.sleep(0.2)
    try:
        yield name
    finally:
        print(f"  Releasing {name}")
        await asyncio.sleep(0.1)


async def main():
    async with AsyncDBConnection() as db:
        r = await db.query("SELECT 1")
        print(f"  Query result: {r}")

    print()

    async with managed_resource("cache-lock") as res:
        print(f"  Using {res}")


if __name__ == "__main__":
    asyncio.run(main())
