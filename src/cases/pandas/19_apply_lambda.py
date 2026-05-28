"""Use apply() for row- or column-wise transformations."""
import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie"],
    "salary": [50000, 80000, 120000]
})

# Element-wise on a Series
df["tax"] = df["salary"].apply(lambda s: s * 0.3 if s > 70000 else s * 0.2)

# Row-wise (axis=1) — access multiple columns
df["summary"] = df.apply(
    lambda row: f"{row['name']} earns {row['salary']}", axis=1
)

print(df)
