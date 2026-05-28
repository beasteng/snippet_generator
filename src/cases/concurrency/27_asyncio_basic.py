"""27 — Basic asyncio coroutine.
INTERVIEW TIP: asyncio is single-threaded cooperative multitasking.
`await` yields control back to the event loop.  Best for I/O-bound
work with many concurrent connections.
"""
import asyncio

async def main():
    print("start")
    await asyncio.sleep(1)
    print("end")

asyncio.run(main())
