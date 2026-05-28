"""05 — Nearest-neighbour search using L2 (Euclidean) distance."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="database for vectors"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT id, content, embedding <-> %s::vector AS distance
        FROM documents ORDER BY distance LIMIT 5
    """, (str(q_emb),)).fetchall()

for r in rows:
    print(f"id={r[0]}  dist={r[2]:.4f}  {r[1][:80]}")
