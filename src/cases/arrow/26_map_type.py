import pyarrow as pa

arr = pa.array(
    [
        [("a", 1), ("b", 2)],
        None,
        [("x", 9)],
    ],
    type=pa.map_(pa.string(), pa.int64()),
)

print(arr)
print("type:", arr.type)
