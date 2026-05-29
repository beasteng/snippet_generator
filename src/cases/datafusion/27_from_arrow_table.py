# DataFusion: Register a PyArrow Table directly
import pyarrow as pa
from datafusion import SessionContext

ctx = SessionContext()
arrow_tbl = pa.table({"a": [1, 2, 3], "b": ["x", "y", "z"]})
ctx.register_record_batches("arrow_data", arrow_tbl.to_batches())
ctx.sql("SELECT * FROM arrow_data WHERE a > 1").show()
