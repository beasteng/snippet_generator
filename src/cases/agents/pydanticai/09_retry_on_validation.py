"""09 — Auto Retry on Validation: Pydantic constraints trigger LLM retry."""
from pydantic import BaseModel, Field
from pydantic_ai import Agent


class Rating(BaseModel):
    score: int = Field(ge=1, le=10)
    reason: str


agent = Agent("openai:gpt-4o-mini", result_type=Rating)

# If the LLM returns score=0 or score=11, PydanticAI auto-retries.
print(agent.run_sync("Rate Python from 1 to 10.").output)
