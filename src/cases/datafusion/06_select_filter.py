# DataFusion: Column projection + row filter via DataFrame API
from datafusion import SessionContext, col

ctx = SessionContext()
df = ctx.from_pydict({"id": [1, 2, 3, 4], "age": [10, 25, 17, 40]})
df.select(col("id"), col("age")).filter(col("age") > 18).show()
