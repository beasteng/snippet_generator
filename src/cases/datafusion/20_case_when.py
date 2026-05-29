# DataFusion: CASE WHEN conditional logic
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"score": [45, 70, 85, 95]})
ctx.register_record_batches("t", [df.collect()])
ctx.sql(
    "SELECT score, CASE "
    "WHEN score >= 90 THEN 'A' "
    "WHEN score >= 80 THEN 'B' "
    "WHEN score >= 70 THEN 'C' "
    "ELSE 'F' END AS grade FROM t"
).show()
