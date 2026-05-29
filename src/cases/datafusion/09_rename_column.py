# DataFusion: Rename a column
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"old_name": [1, 2, 3]})
df.with_column_renamed("old_name", "new_name").show()
