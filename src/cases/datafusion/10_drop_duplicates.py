# DataFusion: Remove duplicate rows via DISTINCT
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"dept": ["eng", "eng", "hr", "hr"], "val": [1, 1, 2, 3]})
ctx.register_record_batches("t", [df.collect()])
ctx.sql("SELECT DISTINCT dept FROM t").show()
