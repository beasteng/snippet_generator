"""02 — Create a documents table with a vector(1536) column."""
import os, psycopg

conn = psycopg.connect(os.environ["DATABASE_URL"])
conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")
conn.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id        bigserial PRIMARY KEY,
        content   text NOT NULL,
        metadata  jsonb DEFAULT '{}',
        embedding vector(1536) NOT NULL
    );
""")
conn.commit()
conn.close()
print("✅ documents table created")
