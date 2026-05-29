# DataFusion: LAG and LEAD window functions
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"month": [1, 2, 3, 4], "sales": [100, 120, 90, 150]})
ctx.register_record_batches("t", [df.collect()])
ctx.sql(
    "SELECT month, sales, "
    "LAG(sales,  1) OVER (ORDER BY month) AS prev_month, "
    "LEAD(sales, 1) OVER (ORDER BY month) AS next_month "
    "FROM t"
).show()
