"""05 — Basic Tool: give the agent a callable function."""
from pydantic_ai import Agent, RunContext

agent = Agent("openai:gpt-4o-mini")


@agent.tool
def double(ctx: RunContext[None], x: int) -> int:
    """Double the input number."""
    return x * 2


print(agent.run_sync("Use the double tool on 21.").output)
