"""
17 — ReAct Agent Loop (Full Implementation)
=============================================
Complete thought → action → observation loop with tool dispatch.
Interview point: This is the core loop of most modern agents.
"""
import re

TOOLS = {
    "search": lambda q: f"Search result for '{q}': Python was created in 1991.",
    "calc":   lambda expr: str(eval(expr, {"__builtins__": {}})),
}

def parse_action(text: str) -> tuple[str, str] | None:
    match = re.search(r"Action:\s*(\w+)\((.*?)\)", text)
    if match:
        return match.group(1), match.group(2).strip("\"'")
    return None

def react_loop(question: str, max_steps: int = 5) -> str:
    transcript = f"Question: {question}\n"
    for step in range(max_steps):
        # Simulate LLM generating thought + action
        if step == 0:
            transcript += "Thought: I should search for this.\n"
            transcript += 'Action: search("Python creation")\n'
        else:
            transcript += "Thought: I now have enough info.\n"
            transcript += "Final Answer: Python was created in 1991 by Guido van Rossum.\n"
            break

        action = parse_action(transcript.split("\n")[-2])
        if action:
            tool_name, arg = action
            result = TOOLS.get(tool_name, lambda x: "Unknown tool")(arg)
            transcript += f"Observation: {result}\n"

    return transcript

if __name__ == "__main__":
    print(react_loop("When was Python created?"))
