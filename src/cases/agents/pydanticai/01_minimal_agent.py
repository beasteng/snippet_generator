"""01 — Minimal Agent: simplest possible PydanticAI usage."""
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini", system_prompt="Answer in one sentence.")

result = agent.run_sync("What is PydanticAI?")
print(result.output)
