import pyarrow as pa
import pyarrow.ipc as ipc

table = pa.table({"id": [1, 2], "name": ["Alice", "Bob"]})
path  = "/tmp/arrow_sample.arrow"

# Write IPC (Feather v2) file
with pa.OSFile(path, "wb") as sink:
    with ipc.new_file(sink, table.schema) as writer:
        writer.write_table(table)

# Read back — zero-copy with memory mapping
with pa.memory_map(path, "r") as source:
    loaded = ipc.open_file(source).read_all()

print(loaded)
