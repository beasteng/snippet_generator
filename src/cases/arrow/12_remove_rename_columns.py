import pyarrow as pa

table = pa.table({"id": [1, 2, 3], "old_name": ["Alice", "Bob", "Cara"]})

table2 = table.rename_columns(["id", "name"])
table3 = table2.drop_columns(["id"])
print(table3)
