# DataFusion: Simulate HAVING by filtering after aggregate
from datafusion import SessionContext, col, functions as F

ctx = SessionContext()
df = ctx.from_pydict({"cat": ["x", "x", "y"], "val": [1, 2, 3]})
agg = df.aggregate([col("cat")], [F.sum(col("val")).alias("total")])
agg.filter(col("total") > 2).show()
