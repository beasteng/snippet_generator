"""Inner merge — only matching keys survive."""
import pandas as pd

employees = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
scores    = pd.DataFrame({"id": [1, 3, 4], "score": [90, 85, 70]})

merged = pd.merge(employees, scores, on="id", how="inner")
print(merged)
# Only id 1 and 3 appear
