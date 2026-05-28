"""Read a CSV file into a DataFrame."""
import pandas as pd

# df = pd.read_csv("data.csv")            # from file
# df = pd.read_csv("data.csv", sep=";")    # custom delimiter
# df = pd.read_csv("url")                  # from URL

# Quick demo with inline data
from io import StringIO
csv_data = "name,age\nAlice,25\nBob,30"
df = pd.read_csv(StringIO(csv_data))
print(df.head())
