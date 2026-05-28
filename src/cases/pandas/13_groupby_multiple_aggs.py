"""Named aggregation — multiple stats in one call."""
import pandas as pd

df = pd.DataFrame({
    "dept":   ["IT", "IT", "HR", "HR", "HR"],
    "salary": [100, 150, 80, 120, 110]
})

result = df.groupby("dept").agg(
    salary_sum  = ("salary", "sum"),
    salary_avg  = ("salary", "mean"),
    salary_max  = ("salary", "max"),
    headcount   = ("salary", "size")
)
print(result)
