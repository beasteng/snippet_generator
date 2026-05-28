import pyarrow as pa

left = pa.table({"id": [1, 2, 3], "name": ["Alice", "Bob", "Cara"]})
right = pa.table({"id": [2, 3, 4], "score": [90, 85, 70]})

inner  = left.join(right, keys="id", join_type="inner")
l_outer = left.join(right, keys="id", join_type="left outer")

print("INNER:\n", inner)
print("LEFT OUTER:\n", l_outer)
