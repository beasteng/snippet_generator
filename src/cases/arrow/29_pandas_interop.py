import pyarrow as pa
import pandas as pd

# Pandas → Arrow (zero-copy when possible)
df    = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
table = pa.Table.from_pandas(df)

# Arrow → Pandas
df2 = table.to_pandas()

print(table)
print(df2)
print("Schema with pandas metadata:", table.schema.pandas_metadata)
