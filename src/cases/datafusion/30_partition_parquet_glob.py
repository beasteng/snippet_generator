# DataFusion: Read multiple Parquet files with glob (partitioned dataset)
import pathlib
import pyarrow as pa
import pyarrow.parquet as pq
from datafusion import SessionContext

pathlib.Path("parts").mkdir(exist_ok=True)
for i, (lo, hi) in enumerate([(1, 3), (4, 6)], start=1):
    tbl = pa.table({"id": list(range(lo, hi + 1)), "part": [i] * 3})
    pq.write_table(tbl, f"parts/part_{i}.parquet")

ctx = SessionContext()
ctx.register_parquet("partitioned", "parts/*.parquet")
ctx.sql(
    "SELECT part, COUNT(*) AS cnt FROM partitioned GROUP BY part ORDER BY part"
).show()
