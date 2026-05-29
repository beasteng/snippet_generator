"""23 — Expect column quantile values to be within ranges."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"amount": [10, 20, 30, 40, 50]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnQuantileValuesToBeBetween(
        column="amount",
        quantile_ranges={
            "quantiles": [0.25, 0.5, 0.75],
            "value_ranges": [[15, 25], [25, 35], [35, 45]],
        },
    )
)
print(result.success)  # True
