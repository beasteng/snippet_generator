import pyarrow as pa

# RecordBatch = fixed-size chunk of a Table (no chunked arrays)
batch = pa.record_batch(
    [pa.array([1, 2]), pa.array(["x", "y"])],
    names=["id", "value"],
)
print(batch)
print("num_rows:", batch.num_rows)
