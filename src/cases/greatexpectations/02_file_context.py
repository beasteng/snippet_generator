"""02 — Create a file-backed Data Context (persists to disk)."""
import great_expectations as gx

context = gx.get_context(mode="file")   # creates gx/ directory
print(context.root_directory)
