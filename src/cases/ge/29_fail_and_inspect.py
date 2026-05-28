"""29 — Intentional failure: inspect validation result details."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"age": [-5, 25, 150, 30]})  # -5 and 150 are out of range
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch = asset.add_batch_definition_whole_dataframe("b").get_batch(
    batch_parameters={"dataframe": df}
)

result = batch.validate(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="age", min_value=0, max_value=120
    )
)

print(f"Success: {result.success}")        # False
print(f"Result:  {result.result}")          # details with unexpected values

if not result.success:
    unexpected = result.result.get("unexpected_count", 0)
    pct = result.result.get("unexpected_percent", 0)
    print(f"  {unexpected} unexpected values ({pct:.1f}%)")
