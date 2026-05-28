"""Add / derive new columns."""
import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob"],
    "salary": [50000, 60000]
})

# Arithmetic
df["bonus"]      = df["salary"] * 0.10
df["total_comp"] = df["salary"] + df["bonus"]

# Conditional (np.where or .where)
import numpy as np
df["level"] = np.where(df["salary"] >= 55000, "Senior", "Junior")

print(df)
