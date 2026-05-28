"""19 — Expect column values to be monotonically increasing."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"seq": [1, 2, 3, 4, 5]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnValuesToBeIncreasing(column="seq")
)
print(result.success)  # True
