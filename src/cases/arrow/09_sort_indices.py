import pyarrow as pa
import pyarrow.compute as pc

table = pa.table({"id": [1, 2, 3, 4], "score": [90, 70, 95, 80]})

idx          = pc.sort_indices(table, sort_keys=[("score", "descending")])
sorted_table = table.take(idx)
print(sorted_table)
