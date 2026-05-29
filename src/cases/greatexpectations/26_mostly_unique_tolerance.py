"""26 — Tolerate some duplicates with 'mostly' on unique check."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"id": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

# Allow up to 10% duplicates
result = batch.validate(
    gx.expectations.ExpectColumnValuesToBeUnique(column="id", mostly=0.9)
)
print(result.success)  # True  (9/10 unique = 90%)
