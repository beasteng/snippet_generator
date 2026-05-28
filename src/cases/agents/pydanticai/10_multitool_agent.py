"""10 — Multi-Tool Agent: register several tools on one agent."""
from pydantic_ai import Agent, RunContext

agent = Agent("openai:gpt-4o-mini")


@agent.tool
def add(ctx: RunContext[None], a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@agent.tool
def multiply(ctx: RunContext[None], a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


print(agent.run_sync("Compute (3 + 4) * 5 using tools.").output)
