import pyarrow as pa
import pyarrow.compute as pc

a = pa.array([10, 20, 30])
b = pa.array([1, 2, 3])

print("add:      ", pc.add(a, b))
print("multiply: ", pc.multiply(a, b))
print("mean:     ", pc.mean(a).as_py())
print("min_max:  ", pc.min_max(a).as_py())
