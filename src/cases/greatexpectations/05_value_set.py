"""05 — Expect column values to be in a set."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"status": ["new", "open", "closed"]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnValuesToBeInSet(
        column="status", value_set=["new", "open", "closed", "resolved"]
    )
)
print(result.success)  # True
