# DataFusion: Add a derived/computed column
from datafusion import SessionContext, col

ctx = SessionContext()
df = ctx.from_pydict({"price": [10.0, 20.0, 30.0], "qty": [2, 3, 1]})
df.with_column("revenue", col("price") * col("qty")).show()
