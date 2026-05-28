"""Create a DataFrame from a dictionary."""
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age":  [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
})

print(df)
# Interview tip: DataFrame is the central pandas data structure —
# always mention it's 2-D, labelled, and column-oriented.
