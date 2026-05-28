"""29 — Union Result Type: agent can return one of several models."""
from pydantic import BaseModel
from pydantic_ai import Agent


class Success(BaseModel):
    message: str
    code: int = 200


class Error(BaseModel):
    error: str
    code: int = 400


agent = Agent("openai:gpt-4o-mini", result_type=Success | Error)  # type: ignore[arg-type]

print(agent.run_sync("Return a success response for user creation.").output)
print(agent.run_sync("Return an error for missing email field.").output)
