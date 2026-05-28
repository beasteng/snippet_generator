"""23 — Streamed Text: print tokens as they arrive."""
import asyncio
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini")


async def main() -> None:
    async with agent.run_stream("Write a haiku about data.") as stream:
        async for chunk in stream.stream_text(delta=True):
            print(chunk, end="", flush=True)
    print()


asyncio.run(main())
