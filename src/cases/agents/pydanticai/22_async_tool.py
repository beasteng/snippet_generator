"""22 — Async Tool: tools can be async functions."""
import asyncio
from pydantic_ai import Agent, RunContext

agent = Agent("openai:gpt-4o-mini")


@agent.tool
async def slow_add(ctx: RunContext[None], a: int, b: int) -> int:
    """Simulate a slow async operation."""
    await asyncio.sleep(0.1)
    return a + b


async def main() -> None:
    result = await agent.run("Use slow_add for 2 and 3.")
    print(result.output)


asyncio.run(main())
