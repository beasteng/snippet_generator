# DataFusion: Register and query a Parquet file
import pathlib
import pyarrow as pa
import pyarrow.parquet as pq
from datafusion import SessionContext

p = pathlib.Path("orders.parquet")
if not p.exists():
    tbl = pa.table({"order_id": [1, 2, 3], "amount": [100.0, 200.0, 150.0]})
    pq.write_table(tbl, p)

ctx = SessionContext()
ctx.register_parquet("orders", str(p))
ctx.sql("SELECT * FROM orders").show()
