# DataFusion: avg / min / max aggregations
from datafusion import SessionContext, col, functions as F

ctx = SessionContext()
df = ctx.from_pydict({"team": ["a", "a", "b", "b"], "pts": [10, 30, 20, 40]})
df.aggregate(
    [col("team")],
    [F.avg(col("pts")).alias("avg"),
     F.min(col("pts")).alias("min"),
     F.max(col("pts")).alias("max")],
).show()
