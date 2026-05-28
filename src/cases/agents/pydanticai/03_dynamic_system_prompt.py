"""03 — Dynamic System Prompt: computed at runtime via decorator."""
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini")


@agent.system_prompt
def add_context() -> str:
    return "You are a concise Python tutor. Keep answers under 50 words."


print(agent.run_sync("Explain decorators.").output)
