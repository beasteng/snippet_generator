"""
28 — State Machine Agent
==========================
Explicit state transitions (like a LangGraph graph).
Interview point: State machines make agent behavior predictable
  and debuggable — this is what LangGraph does under the hood.
"""
from enum import Enum, auto
from dataclasses import dataclass, field

class State(Enum):
    CLASSIFY  = auto()
    RETRIEVE  = auto()
    GENERATE  = auto()
    VERIFY    = auto()
    DONE      = auto()

@dataclass
class AgentState:
    query: str
    state: State = State.CLASSIFY
    category: str = ""
    context: list[str] = field(default_factory=list)
    answer: str = ""
    verified: bool = False

def transition(s: AgentState) -> AgentState:
    if s.state == State.CLASSIFY:
        s.category = "technical" if "agent" in s.query.lower() else "general"
        s.state = State.RETRIEVE
    elif s.state == State.RETRIEVE:
        s.context = [f"Doc about {s.category}"]
        s.state = State.GENERATE
    elif s.state == State.GENERATE:
        s.answer = f"Answer using {len(s.context)} docs for '{s.query}'"
        s.state = State.VERIFY
    elif s.state == State.VERIFY:
        s.verified = len(s.answer) > 10
        s.state = State.DONE
    return s

def run_state_machine(query: str) -> AgentState:
    state = AgentState(query=query)
    while state.state != State.DONE:
        prev = state.state
        state = transition(state)
        print(f"  {prev.name} → {state.state.name}")
    return state

if __name__ == "__main__":
    result = run_state_machine("How do agents use planning?")
    print(f"\nResult: {result.answer} (verified={result.verified})")
