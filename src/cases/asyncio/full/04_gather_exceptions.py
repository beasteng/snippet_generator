"""#4 — gather with return_exceptions: don't let one failure kill everything."""
import asyncio


async def safe():
    await asyncio.sleep(0.5)
    return 42


async def risky():
    await asyncio.sleep(0.2)
    raise RuntimeError("boom")


async def main():
    results = await asyncio.gather(
        safe(), risky(), safe(),
        return_exceptions=True,
    )

    for i, r in enumerate(results):
        if isinstance(r, BaseException):
            print(f"  Task {i}: FAILED — {r!r}")
        else:
            print(f"  Task {i}: OK — {r}")


if __name__ == "__main__":
    asyncio.run(main())
