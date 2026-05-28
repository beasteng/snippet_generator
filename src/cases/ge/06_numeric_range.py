"""06 — Expect column values to be between min and max."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"score": [72, 85, 93]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="score", min_value=0, max_value=100
    )
)
print(result.success)  # True
