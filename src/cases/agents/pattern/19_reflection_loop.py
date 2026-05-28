"""
19 — Self-Reflection / Critique Loop
======================================
Generate → Critique → Revise cycle.
Interview point: Reflection dramatically improves output quality;
  used in Reflexion, LATS, and self-refine papers.
"""

def draft(question: str) -> str:
    return "Initial answer: Agents use LLMs."

def critique(answer: str) -> str:
    issues = []
    if len(answer) < 50:
        issues.append("Too short — add more detail")
    if "example" not in answer.lower():
        issues.append("Missing concrete example")
    return "; ".join(issues) if issues else "Looks good"

def revise(answer: str, feedback: str) -> str:
    return f"{answer} For example, a ReAct agent alternates between thinking and acting. {feedback}"

def reflect_loop(question: str, max_rounds: int = 3) -> str:
    answer = draft(question)
    for round_num in range(max_rounds):
        feedback = critique(answer)
        print(f"  Round {round_num + 1} critique: {feedback}")
        if feedback == "Looks good":
            break
        answer = revise(answer, f"[Addressed: {feedback}]")
    return answer

if __name__ == "__main__":
    final = reflect_loop("What are AI agents?")
    print(f"\nFinal answer:\n{final}")
