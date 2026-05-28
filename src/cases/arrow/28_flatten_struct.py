import pyarrow as pa

table = pa.table({
    "id": [1, 2],
    "meta": pa.array([
        {"country": "US", "active": True},
        {"country": "CA", "active": False},
    ]),
})

flat = table.flatten()
print(flat)
# Columns: id, meta.country, meta.active
