import pyarrow as pa

table = pa.table({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Cara"],
    "age": [30, 25, 28],
})

subset = table.select(["name", "age"])
print(subset)
