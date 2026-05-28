import pyarrow as pa
import pyarrow.compute as pc

ages = pa.array([20, 35, 27, 41])

# Element-wise comparison → boolean array
over_30 = pc.greater_equal(ages, 30)
print(over_30)

# Use it to filter a table
table    = pa.table({"age": ages, "name": pa.array(["A","B","C","D"])})
filtered = table.filter(over_30)
print(filtered)
