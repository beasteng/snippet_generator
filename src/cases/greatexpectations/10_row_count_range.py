"""10 — Expect row count to be within a range."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"x": range(50)})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectTableRowCountToBeBetween(min_value=10, max_value=1000)
)
print(result.success)  # True
