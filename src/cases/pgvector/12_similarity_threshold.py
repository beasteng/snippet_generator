"""12 — Only return results above a cosine similarity threshold."""
import os, psycopg
from openai import OpenAI

THRESHOLD = 0.75

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="billing question"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT id, content,
               1 - (embedding <=> %s::vector) AS sim
        FROM documents
        WHERE 1 - (embedding <=> %s::vector) >= %s
        ORDER BY sim DESC
        LIMIT 10
    """, (str(q_emb), str(q_emb), THRESHOLD)).fetchall()

print(f"Found {len(rows)} results above {THRESHOLD}")
for r in rows:
    print(f"  sim={r[2]:.4f}  {r[1][:60]}")
