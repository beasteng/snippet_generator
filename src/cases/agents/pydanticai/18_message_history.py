"""18 — Message History: multi-turn conversation."""
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini")

r1 = agent.run_sync("My name is Sam.")
r2 = agent.run_sync("What is my name?", message_history=r1.all_messages())
print(r2.output)  # Should mention "Sam"
