"""24 — Streamed Structured Output: stream then collect final model."""
import asyncio
from pydantic import BaseModel
from pydantic_ai import Agent


class Plan(BaseModel):
    title: str
    steps: list[str]


agent = Agent("openai:gpt-4o-mini", result_type=Plan)


async def main() -> None:
    async with agent.run_stream(
        "Create a 3-step learning plan for Python."
    ) as stream:
        result = await stream.get_output()
        print(result)


asyncio.run(main())
