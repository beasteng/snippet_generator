"""17 — Expect proportion of unique values to be within a range."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"x": [1, 1, 2, 3]})  # 3/4 = 0.75 unique
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnProportionOfUniqueValuesToBeBetween(
        column="x", min_value=0.5, max_value=1.0
    )
)
print(result.success)  # True
