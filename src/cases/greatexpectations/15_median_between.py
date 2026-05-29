"""15 — Expect column median to be within a range."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"val": [10, 20, 30, 40, 50]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnMedianToBeBetween(
        column="val", min_value=25, max_value=35
    )
)
print(result.success)  # True  (median = 30)
