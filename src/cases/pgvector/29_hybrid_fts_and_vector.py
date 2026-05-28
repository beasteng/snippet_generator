"""29 — Hybrid: combine Postgres full-text search (tsvector) with vector similarity."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
query  = "machine learning deployment"
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input=query
).data[0].embedding

ALPHA = 0.7  # weight for vector similarity

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    # Ensure tsvector column exists
    conn.execute("""
        ALTER TABLE documents
        ADD COLUMN IF NOT EXISTS tsv tsvector
        GENERATED ALWAYS AS (to_tsvector('english', coalesce(content, ''))) STORED;
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_docs_tsv ON documents USING gin(tsv);")
    conn.commit()

    rows = conn.execute("""
        SELECT id, content,
               ts_rank(tsv, websearch_to_tsquery('english', %s))     AS fts_score,
               1 - (embedding <=> %s::vector)                        AS vec_score,
               %s * (1 - (embedding <=> %s::vector))
                 + (1 - %s) * ts_rank(tsv, websearch_to_tsquery('english', %s)) AS hybrid
        FROM documents
        WHERE tsv @@ websearch_to_tsquery('english', %s)
           OR 1 - (embedding <=> %s::vector) > 0.3
        ORDER BY hybrid DESC
        LIMIT 10
    """, (query, str(q_emb), ALPHA, str(q_emb), ALPHA, query, query, str(q_emb))).fetchall()

for r in rows:
    print(f"id={r[0]}  fts={r[2]:.4f}  vec={r[3]:.4f}  hybrid={r[4]:.4f}  {r[1][:50]}")
