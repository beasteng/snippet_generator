"""08 — Create an HNSW index for fast approximate nearest-neighbour search."""
import os, psycopg

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_documents_hnsw
        ON documents
        USING hnsw (embedding vector_cosine_ops)
        WITH (m = 16, ef_construction = 200);
    """)
    conn.commit()
print("✅ HNSW index created")
