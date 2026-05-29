# DataFusion: Register and query a CSV file
import pathlib
from datafusion import SessionContext

p = pathlib.Path("people.csv")
if not p.exists():
    p.write_text("name,age,city\nalice,30,NYC\nbob,25,LA\ncarol,35,NYC\n")

ctx = SessionContext()
ctx.register_csv("people", str(p))
ctx.sql("SELECT * FROM people").show()
