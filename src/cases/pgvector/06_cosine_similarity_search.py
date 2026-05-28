"""06 — Cosine similarity search (most common for normalized embeddings)."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="semantic search"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT id, content, 1 - (embedding <=> %s::vector) AS similarity
        FROM documents ORDER BY embedding <=> %s::vector LIMIT 5
    """, (str(q_emb), str(q_emb))).fetchall()

for r in rows:
    print(f"id={r[0]}  sim={r[2]:.4f}  {r[1][:80]}")
