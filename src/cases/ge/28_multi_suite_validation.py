"""28 — Multiple suites validated in a single Checkpoint."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"id": [1, 2, 3], "price": [9.99, 19.99, 29.99]})
context = gx.get_context(mode="ephemeral")

ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch_def = asset.add_batch_definition_whole_dataframe("b")

# Suite 1: schema checks
s1 = context.suites.add(gx.ExpectationSuite(name="schema"))
s1.add_expectation(
    gx.expectations.ExpectTableColumnsToMatchSet(column_set=["id", "price"])
)
s1.add_expectation(gx.expectations.ExpectTableRowCountToBeBetween(min_value=1, max_value=100))

# Suite 2: data quality checks
s2 = context.suites.add(gx.ExpectationSuite(name="quality"))
s2.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="id"))
s2.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(column="price", min_value=0, max_value=10000)
)

vd1 = context.validation_definitions.add(
    gx.ValidationDefinition(name="vd1", data=batch_def, suite=s1)
)
vd2 = context.validation_definitions.add(
    gx.ValidationDefinition(name="vd2", data=batch_def, suite=s2)
)

checkpoint = context.checkpoints.add(
    gx.Checkpoint(name="multi_cp", validation_definitions=[vd1, vd2])
)

result = checkpoint.run(batch_parameters={"dataframe": df})
print(f"Overall success: {result.success}")
