import pyarrow as pa

schema = pa.schema([
    ("id", pa.int64()),
    ("meta", pa.struct([
        ("country", pa.string()),
        ("active",  pa.bool_()),
    ])),
])

table = pa.Table.from_pylist([
    {"id": 1, "meta": {"country": "US", "active": True}},
    {"id": 2, "meta": {"country": "CA", "active": False}},
], schema=schema)

print(table)
print(table.schema)
