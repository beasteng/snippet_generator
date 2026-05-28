"""11 — Expect table columns to match an ordered list."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"id": [1], "name": ["a"], "age": [20]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectTableColumnsToMatchOrderedList(
        column_list=["id", "name", "age"]
    )
)
print(result.success)  # True
