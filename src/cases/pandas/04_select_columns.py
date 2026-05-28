"""Select one or multiple columns."""
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "age":  [25, 30],
    "city": ["NY", "LA"]
})

# Single column → Series
print(df["name"])

# Multiple columns → DataFrame
print(df[["name", "age"]])

# With .loc / .iloc
print(df.loc[:, "name":"age"])   # label-based slice (inclusive)
print(df.iloc[:, 0:2])           # position-based slice (exclusive end)
