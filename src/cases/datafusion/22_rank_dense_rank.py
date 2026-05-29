# DataFusion: RANK vs DENSE_RANK comparison
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"name": ["a", "b", "c", "d"], "score": [100, 90, 90, 80]})
ctx.register_record_batches("t", [df.collect()])
ctx.sql(
    "SELECT name, score, "
    "RANK()       OVER (ORDER BY score DESC) AS rnk, "
    "DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rnk "
    "FROM t"
).show()
