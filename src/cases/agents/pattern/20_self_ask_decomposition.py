"""
20 — Self-Ask: Question Decomposition
========================================
Break complex questions into answerable sub-questions.
Interview point: Decomposition is key for multi-hop reasoning.
"""

def decompose(question: str) -> list[str]:
    """Simulate LLM decomposing a complex question."""
    if "compare" in question.lower():
        parts = question.lower().replace("compare", "").strip().split(" and ")
        return [
            f"What are the key features of{parts[0].strip()}?",
            f"What are the key features of{parts[1].strip()}?" if len(parts) > 1 else "",
            "What are the main differences?",
        ]
    return [question]

def answer_subquestion(q: str) -> str:
    return f"Answer to '{q}': [LLM response]"

def self_ask(question: str) -> str:
    subs = decompose(question)
    print(f"Decomposed into {len(subs)} sub-questions:")
    answers = []
    for i, sq in enumerate(subs):
        if not sq:
            continue
        ans = answer_subquestion(sq)
        answers.append(ans)
        print(f"  {i+1}. {sq}\n     → {ans}")

    return f"Combined answer from {len(answers)} sub-answers."

if __name__ == "__main__":
    print(self_ask("Compare Python and JavaScript for AI development"))
