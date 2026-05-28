"""22 — Expect column A < column B (cross-column comparison)."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"start": [1, 2, 3], "end": [2, 3, 4]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnPairValuesAToBeGreaterThanB(
        column_A="end", column_B="start"
    )
)
print(result.success)  # True
