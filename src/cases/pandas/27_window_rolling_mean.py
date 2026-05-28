"""Rolling (sliding window) calculations."""
import pandas as pd

df = pd.DataFrame({
    "day":   range(1, 8),
    "sales": [10, 20, 15, 30, 25, 40, 35]
})

df["rolling_mean_3"] = df["sales"].rolling(window=3).mean()
df["cumsum"]         = df["sales"].cumsum()
df["expanding_mean"] = df["sales"].expanding().mean()

print(df)
