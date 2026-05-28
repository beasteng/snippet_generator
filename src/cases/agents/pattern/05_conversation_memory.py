"""
05 — Conversation Memory (Buffer)
===================================
Append every message to a list; send full history each turn.
Interview point: Simplest memory — O(n) token growth, needs truncation.
"""

class BufferMemory:
    def __init__(self):
        self.messages: list[dict] = []

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})

    def get_messages(self) -> list[dict]:
        return list(self.messages)

def chat(memory: BufferMemory, user_msg: str) -> str:
    memory.add("user", user_msg)
    reply = f"Echo (history={len(memory.messages)}): {user_msg}"
    memory.add("assistant", reply)
    return reply

if __name__ == "__main__":
    mem = BufferMemory()
    print(chat(mem, "Hello"))
    print(chat(mem, "Remember my name is Alex"))
    print(chat(mem, "What is my name?"))
    print("Full history:", mem.get_messages())
