"""01 — Create an ephemeral (in-memory) Data Context."""
import great_expectations as gx

context = gx.get_context(mode="ephemeral")
print(type(context))
# <class 'great_expectations.data_context.EphemeralDataContext'>
