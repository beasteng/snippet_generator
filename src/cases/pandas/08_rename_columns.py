"""Rename columns for cleaner schemas."""
import pandas as pd

df = pd.DataFrame({
    "First Name": ["Alice", "Bob"],
    "years old":  [25, 30]
})

df = df.rename(columns={"First Name": "first_name", "years old": "age"})
print(df)

# Bulk rename with a function
df.columns = df.columns.str.upper()
print(df)
