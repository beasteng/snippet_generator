"""13 — Upsert: insert or update an embedding on conflict."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
text   = "updated document content"
emb    = client.embeddings.create(
    model="text-embedding-3-small", input=text
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    conn.execute("""
        INSERT INTO documents (id, content, embedding)
        VALUES (%s, %s, %s::vector)
        ON CONFLICT (id) DO UPDATE
           SET content   = EXCLUDED.content,
               embedding = EXCLUDED.embedding
    """, (1, text, str(emb)))
    conn.commit()
print("✅ upserted id=1")
