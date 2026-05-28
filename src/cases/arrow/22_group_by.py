import pyarrow as pa

table = pa.table({
    "city":  ["NYC", "NYC", "LA", "LA", "LA"],
    "sales": [10, 20, 5, 7, 8],
})

result = table.group_by("city").aggregate([("sales", "sum")])
print(result)
