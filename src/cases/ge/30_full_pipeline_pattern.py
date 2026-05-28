"""30 — Full production pipeline pattern with conditional raise."""
import great_expectations as gx
import pandas as pd
import sys

# --- 1. Load data ---
df = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "email": ["a@b.com", "c@d.com", "e@f.com", "g@h.com", "bad-email"],
    "age": [25, 30, None, 45, 22],
    "signup_date": ["2025-01-01", "2025-06-15", "2025-12-31", "2026-01-10", "2026-05-28"],
})

# --- 2. Context + data source ---
context = gx.get_context(mode="ephemeral")
ds = context.data_sources.add_pandas("pipeline")
asset = ds.add_dataframe_asset("users")
batch_def = asset.add_batch_definition_whole_dataframe("batch")

# --- 3. Build comprehensive suite ---
suite = context.suites.add(gx.ExpectationSuite(name="user_quality"))

suite.add_expectation(
    gx.expectations.ExpectTableColumnsToMatchSet(
        column_set=["user_id", "email", "age", "signup_date"]
    )
)
suite.add_expectation(gx.expectations.ExpectTableRowCountToBeBetween(min_value=1))
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="user_id"))
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToMatchRegex(
        column="email", regex=r"^[^@]+@[^@]+\.[^@]+$", mostly=0.8
    )
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="age", min_value=0, max_value=120, mostly=0.8
    )
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToMatchStrftimeFormat(
        column="signup_date", strftime_format="%Y-%m-%d"
    )
)

# --- 4. Validation Definition + Checkpoint ---
vd = context.validation_definitions.add(
    gx.ValidationDefinition(name="user_vd", data=batch_def, suite=suite)
)
checkpoint = context.checkpoints.add(
    gx.Checkpoint(name="user_cp", validation_definitions=[vd])
)

# --- 5. Run and act on results ---
result = checkpoint.run(batch_parameters={"dataframe": df})

print(f"Overall success: {result.success}")
if not result.success:
    print("❌ Validation FAILED — blocking pipeline.")
    # In production: raise, alert, or redirect to quarantine
    sys.exit(1)
else:
    print("✅ All checks passed — proceeding with pipeline.")
