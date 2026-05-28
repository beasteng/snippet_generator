"""09 — Create an IVFFlat index (good when data > 1 000 rows)."""
import os, psycopg

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_documents_ivfflat
        ON documents
        USING ivfflat (embedding vector_cosine_ops)
        WITH (lists = 100);
    """)
    conn.commit()
print("✅ IVFFlat index created (lists=100)")
