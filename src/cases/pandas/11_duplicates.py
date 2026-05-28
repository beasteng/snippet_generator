"""Detect and drop duplicate rows."""
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Alice", "Bob"],
    "age":  [25, 30, 25, 31]
})

print("Duplicated?\n", df.duplicated())
print("\nDrop exact dups:\n", df.drop_duplicates())
print("\nDrop dups on 'name' (keep last):\n",
      df.drop_duplicates(subset=["name"], keep="last"))
