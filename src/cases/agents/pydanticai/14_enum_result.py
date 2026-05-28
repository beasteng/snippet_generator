"""14 — Enum Result Type: constrain the LLM to a fixed set of answers."""
from enum import Enum
from pydantic_ai import Agent


class Decision(str, Enum):
    yes = "yes"
    no = "no"
    maybe = "maybe"


agent = Agent("openai:gpt-4o-mini", result_type=Decision)

print(agent.run_sync("Should I refactor this spaghetti code?").output)
