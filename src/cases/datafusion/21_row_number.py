# DataFusion: ROW_NUMBER window function
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"dept": ["eng", "eng", "hr", "hr"], "salary": [90, 70, 80, 60]})
ctx.register_record_batches("emp", [df.collect()])
ctx.sql(
    "SELECT dept, salary, "
    "ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn "
    "FROM emp"
).show()
