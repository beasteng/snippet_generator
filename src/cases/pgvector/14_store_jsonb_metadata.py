"""14 — Store structured JSONB metadata with the embedding."""
import os, json, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
text   = "pgvector supports JSONB metadata"
emb    = client.embeddings.create(
    model="text-embedding-3-small", input=text
).data[0].embedding
meta   = {"source": "docs", "lang": "en", "version": 2}

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    conn.execute(
        "INSERT INTO documents (content, metadata, embedding) "
        "VALUES (%s, %s::jsonb, %s::vector)",
        (text, json.dumps(meta), str(emb)),
    )
    conn.commit()
print("✅ stored with metadata")
