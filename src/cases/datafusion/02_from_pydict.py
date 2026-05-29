# DataFusion: Create DataFrame from a Python dict
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"id": [1, 2, 3], "name": ["alice", "bob", "carol"]})
df.show()
