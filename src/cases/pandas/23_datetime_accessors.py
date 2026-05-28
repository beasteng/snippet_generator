"""Extract date parts with the .dt accessor."""
import pandas as pd

df = pd.DataFrame({
    "ts": pd.to_datetime(["2026-01-01 08:30", "2026-02-15 14:45", "2026-03-20 22:00"])
})

df["year"]     = df["ts"].dt.year
df["month"]    = df["ts"].dt.month
df["day_name"] = df["ts"].dt.day_name()
df["hour"]     = df["ts"].dt.hour
df["quarter"]  = df["ts"].dt.quarter

print(df)
