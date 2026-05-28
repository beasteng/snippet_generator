"""16 — Expect column standard deviation to be within bounds."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3, 4, 5]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnStdevToBeBetween(
        column="x", min_value=1.0, max_value=2.0
    )
)
print(result.success)  # True
