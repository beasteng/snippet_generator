"""11 — Tool Docstrings: the docstring becomes the tool description for the LLM."""
from pydantic_ai import Agent, RunContext

agent = Agent("openai:gpt-4o-mini")


@agent.tool
def capitalize_text(ctx: RunContext[None], text: str) -> str:
    """Capitalize every character in the given text.

    Args:
        text: The text to capitalize.
    """
    return text.upper()


print(agent.run_sync("Use capitalize_text on 'hello world'.").output)
