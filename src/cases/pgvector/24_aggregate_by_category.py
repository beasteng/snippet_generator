"""24 — Find the closest category (group) to a query vector."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="shipping delay"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT metadata->>'category' AS category,
               MIN(embedding <=> %s::vector) AS best_dist
        FROM documents
        WHERE metadata->>'category' IS NOT NULL
        GROUP BY category
        ORDER BY best_dist
        LIMIT 5
    """, (str(q_emb),)).fetchall()

for r in rows:
    print(f"category={r[0]}  best_dist={r[1]:.4f}")
