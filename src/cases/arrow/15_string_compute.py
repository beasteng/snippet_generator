import pyarrow as pa
import pyarrow.compute as pc

arr     = pa.array(["  Alice  ", "Bob", None])
trimmed = pc.utf8_trim_whitespace(arr)
upper   = pc.utf8_upper(trimmed)

print(upper)   # ["ALICE", "BOB", null]
