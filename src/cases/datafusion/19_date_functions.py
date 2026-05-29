# DataFusion: Date casting and part extraction
from datafusion import SessionContext

ctx = SessionContext()
ctx.sql(
    "SELECT CAST('2025-06-15' AS DATE) AS dt, "
    "date_part('year',  CAST('2025-06-15' AS DATE)) AS yr, "
    "date_part('month', CAST('2025-06-15' AS DATE)) AS mo, "
    "date_part('day',   CAST('2025-06-15' AS DATE)) AS dy"
).show()
