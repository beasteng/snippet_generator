"""21 — Async Agent: use `await agent.run()` for async workflows."""
import asyncio
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini")


async def main() -> None:
    result = await agent.run("Give one tip for async Python.")
    print(result.output)


asyncio.run(main())
