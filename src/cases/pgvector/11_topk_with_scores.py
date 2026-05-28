"""11 — Return top-K results with rounded similarity scores."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="refund policy"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT id, content,
               ROUND((1 - (embedding <=> %s::vector))::numeric, 4) AS score
        FROM documents
        ORDER BY embedding <=> %s::vector
        LIMIT 10
    """, (str(q_emb), str(q_emb))).fetchall()

for r in rows:
    print(f"[{r[2]}] {r[1][:80]}")
