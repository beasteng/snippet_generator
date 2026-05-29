"""18 — Expect column values to match a strftime date format."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"created_at": ["2026-01-01", "2026-05-28"]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnValuesToMatchStrftimeFormat(
        column="created_at", strftime_format="%Y-%m-%d"
    )
)
print(result.success)  # True
