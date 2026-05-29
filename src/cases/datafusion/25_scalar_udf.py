# DataFusion: Register a Python scalar UDF
import pyarrow as pa
from datafusion import SessionContext, udf

def double_it(arr: pa.Array) -> pa.Array:
    return pa.array([x.as_py() * 2 for x in arr], type=pa.int64())

ctx = SessionContext()
double_udf = udf(
    double_it,
    input_types=[pa.int64()],
    return_type=pa.int64(),
    volatility="immutable",
    name="double_it",
)
ctx.register_udf(double_udf)
df = ctx.from_pydict({"val": [1, 2, 3, 4]})
ctx.register_record_batches("t", [df.collect()])
ctx.sql("SELECT val, double_it(val) AS doubled FROM t").show()
