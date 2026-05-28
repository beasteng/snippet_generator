"""Concatenate DataFrames vertically (stacking rows)."""
import pandas as pd

df1 = pd.DataFrame({"name": ["Alice"], "age": [25]})
df2 = pd.DataFrame({"name": ["Bob"],   "age": [30]})
df3 = pd.DataFrame({"name": ["Charlie"], "age": [35]})

combined = pd.concat([df1, df2, df3], ignore_index=True)
print(combined)
