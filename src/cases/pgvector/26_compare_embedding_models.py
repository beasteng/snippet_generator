"""26 — Store embeddings from two different models in separate tables."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
text   = "compare different embedding dimensions"

small = client.embeddings.create(model="text-embedding-3-small", input=text).data[0].embedding  # 1536-d
large = client.embeddings.create(model="text-embedding-3-large", input=text).data[0].embedding  # 3072-d

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS docs_small (id bigserial PRIMARY KEY, content text, embedding vector(1536))")
    conn.execute("CREATE TABLE IF NOT EXISTS docs_large (id bigserial PRIMARY KEY, content text, embedding vector(3072))")
    conn.execute("INSERT INTO docs_small (content, embedding) VALUES (%s, %s::vector)", (text, str(small)))
    conn.execute("INSERT INTO docs_large (content, embedding) VALUES (%s, %s::vector)", (text, str(large)))
    conn.commit()
print(f"✅ small dim={len(small)}, large dim={len(large)}")
