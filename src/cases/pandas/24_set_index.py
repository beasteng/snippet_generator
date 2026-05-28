"""Set a column as the DataFrame index."""
import pandas as pd

df = pd.DataFrame({
    "id":   [101, 102, 103],
    "name": ["Alice", "Bob", "Charlie"]
})

df = df.set_index("id")
print(df)
print(df.loc[102])  # fast label-based lookup
