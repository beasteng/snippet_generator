"""06 — Tool + Dependencies: tool reads from injected deps."""
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext


@dataclass
class Deps:
    tax_rate: float


agent = Agent("openai:gpt-4o-mini", deps_type=Deps)


@agent.tool
def price_with_tax(ctx: RunContext[Deps], price: float) -> float:
    """Return price including tax."""
    return round(price * (1 + ctx.deps.tax_rate), 2)


result = agent.run_sync(
    "Calculate final price for 100.", deps=Deps(tax_rate=0.2)
)
print(result.output)
