# DataFusion: Create DataFrame from a list of dicts
from datafusion import SessionContext

ctx = SessionContext()
df = ctx.from_pylist([
    {"product": "apple",  "price": 1.2},
    {"product": "banana", "price": 0.5},
    {"product": "cherry", "price": 3.0},
])
df.show()
