import pyarrow as pa
import pyarrow.compute as pc

# 1. Define explicit schema
schema = pa.schema([
    ("user_id", pa.int64()),
    ("country", pa.string()),
    ("spend",   pa.float64()),
])

# 2. Build table
table = pa.Table.from_pylist([
    {"user_id": 1, "country": "US", "spend": 12.5},
    {"user_id": 2, "country": "CA", "spend": 8.0},
    {"user_id": 3, "country": "US", "spend": 20.0},
    {"user_id": 4, "country": "CA", "spend": 3.5},
    {"user_id": 5, "country": "US", "spend": 7.0},
], schema=schema)

# 3. Filter
us_only = table.filter(pc.equal(table["country"], "US"))

# 4. Aggregate
total_us = pc.sum(us_only["spend"]).as_py()
avg_us   = pc.mean(us_only["spend"]).as_py()

# 5. Group-by across all countries
by_country = table.group_by("country").aggregate([
    ("spend", "sum"),
    ("spend", "mean"),
    ("spend", "count"),
])

print("=== US rows ===")
print(us_only)
print(f"\\nUS total spend: {total_us}")
print(f"US avg   spend: {avg_us}")
print("\\n=== By country ===")
print(by_country)
