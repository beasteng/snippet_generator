"""25 — Model Settings: control temperature, max_tokens, etc."""
from pydantic_ai import Agent
from pydantic_ai.settings import ModelSettings

agent = Agent(
    "openai:gpt-4o-mini",
    model_settings=ModelSettings(temperature=0.0, max_tokens=100),
)

print(agent.run_sync("Summarize Python in one sentence.").output)
