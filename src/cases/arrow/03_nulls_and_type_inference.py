import pyarrow as pa

# Arrow natively supports nulls — no need for sentinels
arr = pa.array([1, None, 3])
print(arr)
print("type:", arr.type)
print("null_count:", arr.null_count)
