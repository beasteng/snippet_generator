"""
22 — Summarizing Memory
=========================
Compress older messages into a summary to fit context windows.
Interview point: Sliding window + summary = constant memory cost.
"""

class SummarizingMemory:
    def __init__(self, max_recent: int = 4):
        self.summary: str = ""
        self.recent: list[dict] = []
        self.max_recent = max_recent

    def add(self, role: str, content: str):
        self.recent.append({"role": role, "content": content})
        if len(self.recent) > self.max_recent:
            overflow = self.recent[:2]  # Summarize oldest 2
            self.recent = self.recent[2:]
            self.summary = self._summarize(self.summary, overflow)

    def _summarize(self, prev_summary: str, messages: list[dict]) -> str:
        new_text = "; ".join(m["content"] for m in messages)
        if prev_summary:
            return f"{prev_summary} | {new_text}"
        return new_text

    def get_context(self) -> list[dict]:
        msgs = []
        if self.summary:
            msgs.append({"role": "system",
                         "content": f"Conversation summary: {self.summary}"})
        msgs.extend(self.recent)
        return msgs

if __name__ == "__main__":
    mem = SummarizingMemory(max_recent=4)
    for i in range(8):
        mem.add("user", f"Message {i}")
        mem.add("assistant", f"Reply {i}")

    print("Summary:", mem.summary)
    print("Recent messages:", len(mem.recent))
    print("Full context:")
    for m in mem.get_context():
        print(f"  [{m['role']}] {m['content'][:60]}")
