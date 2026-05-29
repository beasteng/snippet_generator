"""24 — Build and use an Expectation Suite (multiple rules)."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"id": [1, 2, 3], "age": [18, 25, 40], "status": ["new", "open", "closed"]})
context = gx.get_context(mode="ephemeral")

suite = gx.ExpectationSuite(name="my_suite")
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="id"))
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(column="age", min_value=0, max_value=120)
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeInSet(
        column="status", value_set=["new", "open", "closed"]
    )
)
suite = context.suites.add(suite)

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch_def = asset.add_batch_definition_whole_dataframe("b")

# Create a validation definition
vd = context.validation_definitions.add(
    gx.ValidationDefinition(
        name="my_vd", data=batch_def, suite=suite
    )
)

results = vd.run(batch_parameters={"dataframe": df})
print(results.success)  # True
