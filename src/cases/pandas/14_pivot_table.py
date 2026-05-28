"""Pivot table — Excel-like cross-tabulation with aggregation."""
import pandas as pd

df = pd.DataFrame({
    "dept":  ["IT", "IT", "HR", "HR"],
    "month": ["Jan", "Feb", "Jan", "Feb"],
    "sales": [100, 120, 80, 90]
})

piv = pd.pivot_table(
    df, index="dept", columns="month",
    values="sales", aggfunc="sum", fill_value=0
)
print(piv)
