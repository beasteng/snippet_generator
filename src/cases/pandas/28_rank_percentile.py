"""Rank rows and compute percentiles."""
import pandas as pd

df = pd.DataFrame({
    "student": ["A", "B", "C", "D", "E"],
    "score":   [50, 80, 80, 100, 60]
})

df["rank_avg"]  = df["score"].rank(method="average", ascending=False)
df["rank_min"]  = df["score"].rank(method="min",     ascending=False)
df["pct_rank"]  = df["score"].rank(pct=True)

print(df.sort_values("rank_avg"))
