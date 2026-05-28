"""13 — Nested Pydantic Models: complex structured output."""
from pydantic import BaseModel
from pydantic_ai import Agent


class Author(BaseModel):
    name: str
    email: str | None = None


class Article(BaseModel):
    title: str
    author: Author
    tags: list[str]


agent = Agent("openai:gpt-4o-mini", result_type=Article)

print(agent.run_sync("Return an article about AI safety.").output)
