import pyarrow as pa
import pyarrow.compute as pc

arr     = pa.array(["red", "blue", "red", "green", "blue"])
encoded = pc.dictionary_encode(arr)

print(encoded)
print("type:", encoded.type)
# Dictionary encoding saves memory for low-cardinality strings
