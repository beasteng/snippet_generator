import pyarrow as pa

table  = pa.table({"id": [1, 2, 3], "name": ["Alice", "Bob", "Cara"]})
table2 = table.append_column("age", pa.array([30, 25, 28]))
print(table2)
