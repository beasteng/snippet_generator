"""Drop rows/columns with missing values."""
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":  ["Alice", None, "Charlie"],
    "age":   [25, 30, np.nan],
    "score": [90, np.nan, np.nan]
})

print("Drop any NaN row:\n", df.dropna())
print("\nDrop row only if ALL NaN:\n", df.dropna(how="all"))
print("\nDrop cols with any NaN:\n", df.dropna(axis=1))
print("\nKeep rows with ≥2 non-NaN:\n", df.dropna(thresh=2))
