import pyarrow as pa
import pyarrow.csv as csv
from pathlib import Path

path = Path("/tmp/arrow_sample.csv")
path.write_text("id,name\n1,Alice\n2,Bob\n", encoding="utf-8")

table = csv.read_csv(path)
print(table)

# Write back
csv.write_csv(table, "/tmp/arrow_sample_out.csv")
