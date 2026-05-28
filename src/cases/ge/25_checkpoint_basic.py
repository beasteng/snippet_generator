"""25 — Run a Checkpoint (the standard validation entrypoint)."""
import great_expectations as gx
import pandas as pd

df = pd.DataFrame({"id": [1, 2, 3], "email": ["a@b.com", "c@d.com", "e@f.com"]})
context = gx.get_context(mode="ephemeral")

# Suite
suite = gx.ExpectationSuite(name="email_suite")
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="id"))
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToMatchRegex(
        column="email", regex=r"^[^@]+@[^@]+\.[^@]+$"
    )
)
suite = context.suites.add(suite)

# Data source + batch definition
ds = context.data_sources.add_pandas("pandas")
asset = ds.add_dataframe_asset("asset")
batch_def = asset.add_batch_definition_whole_dataframe("b")

# Validation definition
vd = context.validation_definitions.add(
    gx.ValidationDefinition(name="vd", data=batch_def, suite=suite)
)

# Checkpoint
checkpoint = context.checkpoints.add(
    gx.Checkpoint(name="cp", validation_definitions=[vd])
)

result = checkpoint.run(batch_parameters={"dataframe": df})
print(result.success)  # True
