"""MultiIndex — hierarchical indexing."""
import pandas as pd

df = pd.DataFrame({
    "dept":   ["IT", "IT", "HR", "HR"],
    "team":   ["A",  "B",  "A",  "B"],
    "value":  [10,   20,   30,   40]
})

mi = df.set_index(["dept", "team"])
print(mi)

# Select IT department
print(mi.loc["IT"])

# Select IT, team B
print(mi.loc[("IT", "B")])
