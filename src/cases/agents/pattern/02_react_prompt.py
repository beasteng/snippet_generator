"""
02 — ReAct Prompt Skeleton
============================
Thought → Action → Observation loop (the foundation of most agents).
Interview point: ReAct = Reasoning + Acting in alternating steps.
"""

REACT_PROMPT = """Answer the question using this format:

Thought: reason about what to do
Action: tool_name(args)
Observation: result from tool
... (repeat as needed)
Final Answer: your answer

Question: {question}
"""

def build_prompt(question: str) -> str:
    return REACT_PROMPT.format(question=question)

if __name__ == "__main__":
    print(build_prompt("What is the population of France?"))
