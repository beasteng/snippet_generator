"""28 — Multiple System Prompts: stack several prompt decorators."""
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini")


@agent.system_prompt
def persona() -> str:
    return "You are a senior Python developer."


@agent.system_prompt
def rules() -> str:
    return "Always include code examples. Be concise."


@agent.system_prompt
def format_rule() -> str:
    return "Format output as Markdown."


print(agent.run_sync("Explain the GIL in Python.").output)
