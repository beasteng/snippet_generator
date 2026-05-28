import pyarrow as pa

arr = pa.array([1, None, 3], type=pa.float32())
print(arr)
print("type:", arr.type)
