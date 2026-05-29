# DataFusion: Convert result to a Pandas DataFrame
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"x": [10, 20, 30], "y": [1.1, 2.2, 3.3]})
pandas_df = df.collect()[0].to_pandas()
print(type(pandas_df))
print(pandas_df)
