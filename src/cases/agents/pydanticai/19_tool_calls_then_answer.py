"""19 — Tool Call + Final Answer: agent uses a tool then summarizes."""
from pydantic_ai import Agent, RunContext

agent = Agent("openai:gpt-4o-mini")


@agent.tool
def square(ctx: RunContext[None], x: int) -> int:
    """Return x squared."""
    return x * x


print(agent.run_sync("Square 12, then explain the result.").output)
