"""Concatenate DataFrames horizontally (adding columns)."""
import pandas as pd

names  = pd.DataFrame({"name": ["Alice", "Bob"]})
ages   = pd.DataFrame({"age": [25, 30]})
cities = pd.DataFrame({"city": ["NY", "LA"]})

combined = pd.concat([names, ages, cities], axis=1)
print(combined)
