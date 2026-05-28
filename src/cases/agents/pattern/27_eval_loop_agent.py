"""
27 — Evaluation Loop for Agents
==================================
Run agent on test cases, compute metrics, iterate.
Interview point: Always evaluate your agent on a held-out dataset
  before deploying.
"""
from dataclasses import dataclass

@dataclass
class TestCase:
    query: str
    expected: str

@dataclass
class EvalResult:
    query: str
    predicted: str
    expected: str
    correct: bool

def dummy_agent(query: str) -> str:
    """Simulated agent."""
    answers = {"capital of France": "Paris", "2+2": "4", "largest planet": "Jupiter"}
    for key, val in answers.items():
        if key in query.lower():
            return val
    return "I don't know"

def evaluate(agent_fn, test_cases: list[TestCase]) -> list[EvalResult]:
    results = []
    for tc in test_cases:
        pred = agent_fn(tc.query)
        results.append(EvalResult(
            query=tc.query,
            predicted=pred,
            expected=tc.expected,
            correct=pred.strip().lower() == tc.expected.strip().lower(),
        ))
    return results

if __name__ == "__main__":
    tests = [
        TestCase("What is the capital of France?", "Paris"),
        TestCase("What is 2+2?", "4"),
        TestCase("What is the largest planet?", "Jupiter"),
        TestCase("Who wrote Python?", "Guido van Rossum"),
    ]
    results = evaluate(dummy_agent, tests)
    correct = sum(1 for r in results if r.correct)
    total = len(results)
    print(f"Score: {correct}/{total} ({correct/total:.0%})\n")
    for r in results:
        status = "✓" if r.correct else "✗"
        print(f"  {status} {r.query}")
        if not r.correct:
            print(f"    Expected: {r.expected}, Got: {r.predicted}")
