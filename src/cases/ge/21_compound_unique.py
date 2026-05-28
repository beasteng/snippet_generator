"""21 — Expect compound columns to be unique together."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"first": ["a", "a", "b"], "second": ["x", "y", "x"]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectCompoundColumnsToBeUnique(
        column_list=["first", "second"]
    )
)
print(result.success)  # True
