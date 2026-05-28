"""Filter rows with boolean conditions."""
import pandas as pd

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Diana"],
    "age":    [25, 30, 35, 28],
    "dept":   ["IT", "HR", "IT", "HR"]
})

# Single condition
print(df[df["age"] > 28])

# Multiple conditions (use & | ~, with parentheses)
print(df[(df["age"] > 25) & (df["dept"] == "IT")])

# .query() — cleaner for complex filters
print(df.query("age > 25 and dept == 'IT'"))

# .isin()
print(df[df["dept"].isin(["IT", "Finance"])])
