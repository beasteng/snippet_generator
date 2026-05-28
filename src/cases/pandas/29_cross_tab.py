"""Crosstab — frequency table of two categorical columns."""
import pandas as pd

df = pd.DataFrame({
    "dept":   ["IT", "IT", "HR", "HR", "IT"],
    "gender": ["M",  "F",  "F",  "M",  "F"]
})

ct = pd.crosstab(df["dept"], df["gender"], margins=True)
print(ct)

# Normalize to show proportions
ct_pct = pd.crosstab(df["dept"], df["gender"], normalize="index")
print("\nProportions:\n", ct_pct)
