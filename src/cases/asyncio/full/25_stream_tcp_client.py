"""#25 — TCP client that connects to the echo server from #24."""
import asyncio


async def main():
    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    for msg in ["Hello", "Asyncio", "World"]:
        print(f"  [client] sending: {msg!r}")
        writer.write(msg.encode())
        await writer.drain()

        data = await reader.read(1024)
        print(f"  [client] received echo: {data.decode()!r}")

    writer.close()
    await writer.wait_closed()
    print("  [client] disconnected")


if __name__ == "__main__":
    asyncio.run(main())
