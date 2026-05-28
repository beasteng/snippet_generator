"""08 — Result Validator: post-validate the LLM's structured output."""
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext


class CityAnswer(BaseModel):
    city: str
    country: str


agent = Agent("openai:gpt-4o-mini", result_type=CityAnswer)


@agent.result_validator
def validate(ctx: RunContext[None], value: CityAnswer) -> CityAnswer:
    if not value.city.strip():
        raise ValueError("city must not be empty")
    return value


print(agent.run_sync("Return Paris, France.").output)
