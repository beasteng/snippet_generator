"""13 — 'mostly' keyword: tolerate some nulls."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"x": [1, None, 3, 4, 5]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

# 80% of values must be non-null (4/5 = 80%)
result = batch.validate(
    gx.expectations.ExpectColumnValuesToNotBeNull(column="x", mostly=0.8)
)
print(result.success)  # True
