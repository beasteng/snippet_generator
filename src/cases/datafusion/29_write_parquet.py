# DataFusion: Write a filtered result out to a Parquet file
import pyarrow as pa
import pyarrow.parquet as pq
from datafusion import SessionContext, col

ctx = SessionContext()
df = ctx.from_pydict({"id": [1, 2, 3], "val": [10, 20, 30]})
batches = df.filter(col("val") > 10).collect()
pq.write_table(pa.Table.from_batches(batches), "output_filtered.parquet")
print("Written → output_filtered.parquet")
