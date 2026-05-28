import pyarrow as pa
import pyarrow.parquet as pq

table = pa.table({"id": [1, 2], "name": ["Alice", "Bob"]})
path  = "/tmp/arrow_sample.parquet"

pq.write_table(table, path, compression="snappy")
loaded = pq.read_table(path)
print(loaded)
print("metadata:", pq.read_metadata(path))
