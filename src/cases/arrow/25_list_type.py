import pyarrow as pa

arr = pa.array([[1, 2], None, [3, 4, 5]])
print(arr)
print("type:", arr.type)
print("values buffer:", arr.values)
