# DataFusion: Cross join (cartesian product)
from datafusion import SessionContext

ctx = SessionContext()
a = ctx.from_pydict({"color": ["red", "blue"]})
b = ctx.from_pydict({"size":  ["S", "M", "L"]})
ctx.register_record_batches("a", [a.collect()])
ctx.register_record_batches("b", [b.collect()])
ctx.sql("SELECT color, size FROM a CROSS JOIN b").show()
