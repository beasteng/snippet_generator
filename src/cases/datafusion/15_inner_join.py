# DataFusion: Inner join two DataFrames via SQL
from datafusion import SessionContext

ctx = SessionContext()
users  = ctx.from_pydict({"id": [1, 2, 3], "name": ["alice", "bob", "carol"]})
orders = ctx.from_pydict({"user_id": [1, 2, 4], "amount": [100, 200, 300]})
ctx.register_record_batches("users",  [users.collect()])
ctx.register_record_batches("orders", [orders.collect()])
ctx.sql(
    "SELECT u.name, o.amount "
    "FROM users u INNER JOIN orders o ON u.id = o.user_id"
).show()
