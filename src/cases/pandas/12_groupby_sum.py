"""GroupBy — the split-apply-combine pattern."""
import pandas as pd

df = pd.DataFrame({
    "dept":   ["IT", "IT", "HR", "HR"],
    "salary": [100, 150, 80, 120]
})

print(df.groupby("dept")["salary"].sum())
print()
print(df.groupby("dept")["salary"].mean())
