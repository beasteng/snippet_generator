# DataFusion: GROUP BY with count + sum
from datafusion import SessionContext, col, functions as F

ctx = SessionContext()
df = ctx.from_pydict({"dept": ["eng", "eng", "hr"], "salary": [90, 110, 70]})
df.aggregate(
    [col("dept")],
    [F.count(col("salary")).alias("headcount"),
     F.sum(col("salary")).alias("total_pay")],
).show()
