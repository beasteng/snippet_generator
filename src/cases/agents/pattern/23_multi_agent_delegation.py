"""
23 — Multi-Agent Delegation (Supervisor Pattern)
==================================================
A supervisor agent delegates to specialist agents.
Interview point: This is the architecture used in CrewAI and
  LangGraph's multi-agent examples.
"""

class Agent:
    def __init__(self, name: str, expertise: str):
        self.name = name
        self.expertise = expertise

    def handle(self, task: str) -> str:
        return f"[{self.name}] Handled '{task}' with {self.expertise} expertise"

class Supervisor:
    def __init__(self, agents: list[Agent]):
        self.agents = {a.expertise: a for a in agents}

    def delegate(self, task: str) -> str:
        # Simple keyword routing (LLM would do this in production)
        task_lower = task.lower()
        for expertise, agent in self.agents.items():
            if expertise in task_lower:
                return agent.handle(task)
        # Default to first agent
        default = next(iter(self.agents.values()))
        return default.handle(task)

if __name__ == "__main__":
    team = Supervisor([
        Agent("CodeBot", "code"),
        Agent("ResearchBot", "research"),
        Agent("WriterBot", "writing"),
    ])
    tasks = [
        "Write code for a binary search",
        "Research latest transformer architectures",
        "Writing a blog post about agents",
    ]
    for task in tasks:
        print(team.delegate(task))
