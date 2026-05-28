"""Fill missing values — scalar, method, or aggregation."""
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":  ["Alice", None, "Charlie", "Diana"],
    "age":   [25, np.nan, 35, np.nan],
    "score": [np.nan, 80, 90, np.nan]
})

df["name"]  = df["name"].fillna("Unknown")
df["age"]   = df["age"].fillna(df["age"].median())
df["score"] = df["score"].ffill()          # forward fill

print(df)
