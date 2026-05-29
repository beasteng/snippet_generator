# DataFusion: Approx distinct count (HyperLogLog)
from datafusion import SessionContext, col, functions as F

ctx = SessionContext()
df = ctx.from_pydict({"user_id": [1, 1, 2, 3, 3, 3, 4]})
df.aggregate(
    [],
    [F.approx_distinct(col("user_id")).alias("approx_unique")]
).show()
