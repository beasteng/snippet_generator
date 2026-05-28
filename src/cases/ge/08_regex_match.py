"""08 — Expect column values to match a regex (email pattern)."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"email": ["alice@example.com", "bob@test.org"]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnValuesToMatchRegex(
        column="email", regex=r"^[^@]+@[^@]+\.[^@]+$"
    )
)
print(result.success)  # True
