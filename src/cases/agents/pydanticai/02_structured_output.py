"""02 — Structured Output: force the LLM to return a Pydantic model."""
from pydantic import BaseModel
from pydantic_ai import Agent


class Answer(BaseModel):
    summary: str
    confidence: float


agent = Agent("openai:gpt-4o-mini", result_type=Answer)

result = agent.run_sync("Explain PydanticAI briefly.")
print(result.output)          # Answer(summary='...', confidence=0.95)
print(result.output.summary)  # access fields directly
