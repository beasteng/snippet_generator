import pyarrow as pa
import pyarrow.compute as pc

arr    = pa.array([1, 2, 3], type=pa.int32())
casted = pc.cast(arr, pa.float64())

print(casted)
print("type:", casted.type)
