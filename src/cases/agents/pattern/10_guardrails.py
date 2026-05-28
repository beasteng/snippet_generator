"""
10 — Input/Output Guardrails
==============================
Block disallowed topics; validate output format.
Interview point: Safety guardrails are mandatory in production agents.
"""
from dataclasses import dataclass

BLOCKED_TERMS = {"password", "secret", "hack", "exploit"}

@dataclass
class GuardrailResult:
    allowed: bool
    reason: str = ""

def check_input(query: str) -> GuardrailResult:
    words = set(query.lower().split())
    blocked = words & BLOCKED_TERMS
    if blocked:
        return GuardrailResult(False, f"Blocked terms: {blocked}")
    return GuardrailResult(True)

def check_output(response: str, max_len: int = 500) -> GuardrailResult:
    if len(response) > max_len:
        return GuardrailResult(False, "Response too long")
    if any(term in response.lower() for term in BLOCKED_TERMS):
        return GuardrailResult(False, "Output contains blocked content")
    return GuardrailResult(True)

if __name__ == "__main__":
    print(check_input("Tell me the password"))
    print(check_input("What is Python?"))
    print(check_output("Here is a safe answer."))
    print(check_output("x" * 600))
