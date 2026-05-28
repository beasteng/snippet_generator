"""17 — Practical Use-Case: structured Todo item generation."""
from pydantic import BaseModel
from pydantic_ai import Agent


class Todo(BaseModel):
    task: str
    priority: int  # 1=highest
    done: bool = False


agent = Agent("openai:gpt-4o-mini", result_type=Todo)

print(agent.run_sync("Create a todo: fix failing tests, priority 1.").output)
