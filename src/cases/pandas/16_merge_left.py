"""Left merge — keep all rows from left table."""
import pandas as pd

employees = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
scores    = pd.DataFrame({"id": [1, 3, 4], "score": [90, 85, 70]})

merged = pd.merge(employees, scores, on="id", how="left")
print(merged)
# Bob (id=2) has NaN score — no match on right side
