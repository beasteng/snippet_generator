"""09 — Expect the table to have an exact row count."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectTableRowCountToEqual(value=3)
)
print(result.success)  # True
