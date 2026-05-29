# DataFusion: Sort descending + limit rows
from datafusion import SessionContext, col

ctx = SessionContext()
df = ctx.from_pydict({"name": ["c", "a", "b"], "score": [30, 10, 20]})
df.sort(col("score").sort(ascending=False)).limit(2).show()
