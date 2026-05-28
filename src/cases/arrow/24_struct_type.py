import pyarrow as pa

data = pa.array([
    {"x": 1, "y": "a"},
    {"x": 2, "y": "b"},
    None,
])

print(data)
print("type:", data.type)
