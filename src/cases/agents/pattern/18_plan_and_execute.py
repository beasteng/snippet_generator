"""
18 — Plan-and-Execute Agent
==============================
Create a plan, then execute each step.
Interview point: Separating planning from execution improves reliability
  and lets you verify/revise the plan before acting.
"""
from dataclasses import dataclass

@dataclass
class Step:
    description: str
    tool: str
    status: str = "pending"
    result: str = ""

def create_plan(task: str) -> list[Step]:
    """Simulate LLM generating a plan."""
    return [
        Step("Search for relevant info", "search"),
        Step("Extract key facts", "extract"),
        Step("Compose final answer", "generate"),
    ]

def execute_step(step: Step) -> Step:
    """Execute a single plan step."""
    step.result = f"Completed: {step.description} using {step.tool}"
    step.status = "done"
    return step

def plan_and_execute(task: str) -> list[Step]:
    plan = create_plan(task)
    print(f"Plan ({len(plan)} steps):")
    for i, step in enumerate(plan):
        print(f"  {i+1}. [{step.tool}] {step.description}")

    print("\nExecuting:")
    for step in plan:
        execute_step(step)
        print(f"  ✓ {step.result}")

    return plan

if __name__ == "__main__":
    plan_and_execute("Summarize the latest AI research trends")
