"""04 — Dependencies: inject runtime context into prompts."""
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext


@dataclass
class Deps:
    language: str


agent = Agent("openai:gpt-4o-mini", deps_type=Deps)


@agent.system_prompt
def prompt(ctx: RunContext[Deps]) -> str:
    return f"Always answer in {ctx.deps.language}."


result = agent.run_sync("What is an LLM?", deps=Deps(language="English"))
print(result.output)
