import pyarrow as pa

table  = pa.table({"id": [1, 2, 3, 4], "name": ["a", "b", "c", "d"]})
picked = table.take(pa.array([3, 1]))
print(picked)
