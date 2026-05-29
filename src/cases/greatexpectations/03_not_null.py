"""03 — Expect column values to not be null."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("people")
batch = asset.add_batch_definition_whole_dataframe("batch").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnValuesToNotBeNull(column="name")
)
print(result.success)  # True
