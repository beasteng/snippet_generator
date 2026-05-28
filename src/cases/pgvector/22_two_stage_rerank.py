"""22 — Two-stage search: broad ANN retrieve → precise re-rank."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="enterprise knowledge base"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        WITH candidates AS (
            SELECT id, content, embedding
            FROM documents
            ORDER BY embedding <=> %s::vector
            LIMIT 50              -- broad recall
        )
        SELECT id, content,
               1 - (embedding <=> %s::vector) AS sim
        FROM candidates
        ORDER BY sim DESC
        LIMIT 10                  -- precise top-10
    """, (str(q_emb), str(q_emb))).fetchall()

for r in rows:
    print(f"sim={r[2]:.4f}  {r[1][:60]}")
