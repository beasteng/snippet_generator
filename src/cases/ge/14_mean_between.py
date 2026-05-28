"""14 — Expect column mean to be within a range."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"score": [10, 20, 30]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnMeanToBeBetween(
        column="score", min_value=15, max_value=25
    )
)
print(result.success)  # True  (mean = 20)
