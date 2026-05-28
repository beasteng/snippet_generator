"""01 — Enable the pgvector extension on a Postgres database."""
import os, psycopg

conn = psycopg.connect(os.environ["DATABASE_URL"])
conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")
conn.commit()
conn.close()
print("✅ pgvector extension is ready")
