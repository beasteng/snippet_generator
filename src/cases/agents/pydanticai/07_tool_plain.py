"""07 — Plain Tool (no RunContext): simpler signature when deps aren't needed."""
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini")


@agent.tool_plain
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


print(agent.run_sync("Call greet with Ada.").output)
