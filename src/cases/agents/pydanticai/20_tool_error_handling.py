"""20 — Tool Error Handling: raise ValueError to signal tool failure to LLM."""
from pydantic_ai import Agent, RunContext

agent = Agent("openai:gpt-4o-mini")


@agent.tool
def divide(ctx: RunContext[None], a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


print(agent.run_sync("Divide 10 by 2, then try 5 by 0.").output)
