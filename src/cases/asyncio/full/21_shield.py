"""#21 — asyncio.shield: protect critical work from cancellation."""
import asyncio


async def critical_db_write(data: str) -> str:
    print(f"  [db] writing '{data}'...")
    await asyncio.sleep(2)
    print(f"  [db] write committed!")
    return "committed"


async def main():
    task = asyncio.create_task(
        asyncio.shield(critical_db_write("important_record"))
    )

    await asyncio.sleep(0.5)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("  Outer wrapper cancelled, but DB write continues in background")

    await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(main())
