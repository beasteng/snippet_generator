"""20 — Expect table columns to match a set (any order)."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"name": ["x"], "id": [1], "age": [20]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectTableColumnsToMatchSet(
        column_set=["id", "name", "age"]
    )
)
print(result.success)  # True
