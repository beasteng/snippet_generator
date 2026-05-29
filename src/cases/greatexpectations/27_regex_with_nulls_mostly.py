"""27 — Combine regex + mostly to tolerate nulls gracefully."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"code": ["AB-123", "CD-456", None, "EF-789", None]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

# Non-null values should match pattern; tolerate 60%+ match
result = batch.validate(
    gx.expectations.ExpectColumnValuesToMatchRegex(
        column="code", regex=r"^[A-Z]{2}-\d{3}$", mostly=0.6
    )
)
print(result.success)  # True
