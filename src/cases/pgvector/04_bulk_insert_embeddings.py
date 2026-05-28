"""04 — Batch-embed several texts and bulk-insert."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
texts  = [
    "Cats are independent creatures.",
    "Dogs are loyal companions.",
    "PostgreSQL is the world's most advanced open-source database.",
    "Vector search powers modern AI applications.",
    "Embeddings capture semantic meaning of text.",
]
response = client.embeddings.create(model="text-embedding-3-small", input=texts)
embeddings = [item.embedding for item in response.data]

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    with conn.cursor() as cur:
        for text, emb in zip(texts, embeddings):
            cur.execute(
                "INSERT INTO documents (content, embedding) VALUES (%s, %s::vector)",
                (text, str(emb)),
            )
    conn.commit()
print(f"✅ inserted {len(texts)} rows")
