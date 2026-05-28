"""Parse strings to datetime and filter by date range."""
import pandas as pd

df = pd.DataFrame({
    "event": ["Launch", "Update", "Retire"],
    "date":  ["2025-01-15", "2025-06-20", "2026-01-10"]
})

df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)

# Filter to 2025 only
mask = (df["date"] >= "2025-01-01") & (df["date"] < "2026-01-01")
print(df[mask])
