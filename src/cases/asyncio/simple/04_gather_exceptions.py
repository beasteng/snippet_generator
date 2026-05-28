"""Error handling with gather(return_exceptions=True)."""
import asyncio


async def ok():
    return "ok"


async def bad():
    raise ValueError("fail")


async def main():
    results = await asyncio.gather(ok(), bad(), return_exceptions=True)
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            print(f"Task {i} failed: {r}")
        else:
            print(f"Task {i} succeeded: {r}")


if __name__ == "__main__":
    asyncio.run(main())
