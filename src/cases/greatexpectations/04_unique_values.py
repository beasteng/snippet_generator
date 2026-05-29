"""04 — Expect column values to be unique."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"id": [1, 2, 3]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnValuesToBeUnique(column="id")
)
print(result.success)  # True
