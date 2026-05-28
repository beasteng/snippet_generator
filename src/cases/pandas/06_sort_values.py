"""Sort a DataFrame by one or more columns."""
import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie"],
    "age":    [30, 25, 35],
    "salary": [70000, 60000, 70000]
})

print(df.sort_values("age"))
print(df.sort_values(["salary", "age"], ascending=[False, True]))
