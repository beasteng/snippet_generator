"""15 — Housekeeping: delete rows with NULL content or embedding."""
import os, psycopg

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    result = conn.execute(
        "DELETE FROM documents WHERE content IS NULL OR embedding IS NULL"
    )
    conn.commit()
print(f"✅ deleted {result.rowcount} rows")
