import pyarrow as pa

t1 = pa.table({"id": [1, 2], "name": ["Alice", "Bob"]})
t2 = pa.table({"id": [3],    "name": ["Cara"]})

combined = pa.concat_tables([t1, t2])
print(combined)
