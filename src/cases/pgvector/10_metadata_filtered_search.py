"""10 — Combine JSONB metadata filter with vector search."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="payment issue"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT id, content
        FROM documents
        WHERE metadata->>'category' = 'support'
        ORDER BY embedding <=> %s::vector
        LIMIT 5
    """, (str(q_emb),)).fetchall()

print(rows)
