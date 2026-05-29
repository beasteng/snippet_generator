# DataFusion: CTE (WITH clause) + filtered subquery
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({
    "region": ["east", "east", "west", "west"],
    "sales":  [100, 200, 150, 50],
})
ctx.register_record_batches("sales_data", [df.collect()])
ctx.sql(
    "WITH regional_totals AS ("
    "  SELECT region, SUM(sales) AS total FROM sales_data GROUP BY region"
    ") "
    "SELECT region, total FROM regional_totals WHERE total > 200 ORDER BY total DESC"
).show()
