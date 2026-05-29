# DataFusion: upper / length / concat string functions
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pydict({"first": ["alice", "bob"], "last": ["smith", "jones"]})
ctx.register_record_batches("t", [df.collect()])
ctx.sql(
    "SELECT upper(first) AS first_up, length(last) AS last_len, "
    "concat(first, ' ', last) AS full_name FROM t"
).show()
