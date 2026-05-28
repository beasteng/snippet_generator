import pyarrow as pa

table = pa.table({"id": [1, 2, 3, 4], "age": [20, 35, 27, 41]})

mask     = pa.array([False, True, False, True])
filtered = table.filter(mask)
print(filtered)
