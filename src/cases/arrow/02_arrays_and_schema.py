import pyarrow as pa

ids   = pa.array([1, 2, 3], type=pa.int64())
names = pa.array(["Alice", "Bob", "Cara"], type=pa.string())

schema = pa.schema([("id", pa.int64()), ("name", pa.string())])
table  = pa.Table.from_arrays([ids, names], schema=schema)

print(schema)
print(table)
