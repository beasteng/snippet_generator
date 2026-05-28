"""26 — Config as Deps: inject application config into the agent."""
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext


@dataclass
class Config:
    app_name: str
    version: str
    debug: bool = False


agent = Agent("openai:gpt-4o-mini", deps_type=Config)


@agent.system_prompt
def sys(ctx: RunContext[Config]) -> str:
    cfg = ctx.deps
    return (
        f"You are the assistant for {cfg.app_name} v{cfg.version}. "
        f"Debug mode: {cfg.debug}."
    )


result = agent.run_sync(
    "Introduce yourself.", deps=Config("InterviewPrep", "2.0", debug=True)
)
print(result.output)
