"""Quickly inspect a DataFrame — shape, dtypes, stats."""
import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie"],
    "age":    [25, 30, 35],
    "salary": [50000, 60000, 70000]
})

print("Shape  :", df.shape)        # (rows, cols)
print("Columns:", df.columns.tolist())
print("Dtypes :\n", df.dtypes)
print("\nInfo:")
df.info()
print("\nDescribe:\n", df.describe())
