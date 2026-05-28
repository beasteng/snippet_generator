"""
04 — Tool Registry Pattern
============================
Register tools in a dict; select by name.
Interview point: This is how frameworks like LangChain store tools internally.
"""
from typing import Callable

TOOL_REGISTRY: dict[str, Callable] = {}

def tool(name: str):
    """Decorator to register a tool."""
    def decorator(fn: Callable):
        TOOL_REGISTRY[name] = fn
        return fn
    return decorator

@tool("calculator")
def calculator(expr: str) -> str:
    return str(eval(expr, {"__builtins__": {}}))

@tool("weather")
def weather(city: str) -> str:
    return f"Weather in {city}: 22°C, sunny"

def dispatch(tool_name: str, arg: str) -> str:
    if tool_name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool: {tool_name}")
    return TOOL_REGISTRY[tool_name](arg)

if __name__ == "__main__":
    print(dispatch("calculator", "2 + 3 * 4"))
    print(dispatch("weather", "London"))
    print("Available tools:", list(TOOL_REGISTRY.keys()))
