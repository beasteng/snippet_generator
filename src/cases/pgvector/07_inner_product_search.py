"""07 — Max inner-product search (useful for non-normalized embeddings)."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="recommendation engine"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT id, content
        FROM documents ORDER BY embedding <#> %s::vector LIMIT 5
    """, (str(q_emb),)).fetchall()

for r in rows:
    print(r)
