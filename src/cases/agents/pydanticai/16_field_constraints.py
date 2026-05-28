"""16 — Field Constraints: Pydantic Field validations auto-retry the LLM."""
from pydantic import BaseModel, Field
from pydantic_ai import Agent


class Profile(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0, le=150)
    bio: str = Field(max_length=200)


agent = Agent("openai:gpt-4o-mini", result_type=Profile)

print(agent.run_sync("Return a profile for Ada Lovelace, age 28.").output)
