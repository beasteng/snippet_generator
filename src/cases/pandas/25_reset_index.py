"""Reset index back to a regular column."""
import pandas as pd

df = pd.DataFrame({
    "id":   [101, 102, 103],
    "name": ["Alice", "Bob", "Charlie"]
}).set_index("id")

df_reset = df.reset_index()
print(df_reset)
print(df_reset.columns.tolist())  # ['id', 'name']
