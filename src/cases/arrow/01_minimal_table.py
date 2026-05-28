import pyarrow as pa

# Fastest way to create an in-memory columnar table
table = pa.table({"id": [1, 2, 3], "name": ["Alice", "Bob", "Cara"]})
print(table)
print(table.to_pydict())
