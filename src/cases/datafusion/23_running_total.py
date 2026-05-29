# DataFusion: Running total with SUM window function
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"day": [1, 2, 3, 4], "revenue": [100, 200, 150, 300]})
ctx.register_record_batches("sales", [df.collect()])
ctx.sql(
    "SELECT day, revenue, "
    "SUM(revenue) OVER (ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) "
    "AS running_total FROM sales"
).show()
