# DataFusion: Run inline SQL with no data source
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.sql("SELECT 1 AS one, 2 AS two, 1 + 2 AS three")
df.show()
