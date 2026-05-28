"""03 — Embed one text and INSERT into pgvector."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
conn   = psycopg.connect(os.environ["DATABASE_URL"])

text = "PostgreSQL with pgvector stores embeddings efficiently."
emb  = client.embeddings.create(
    model="text-embedding-3-small", input=text
).data[0].embedding

conn.execute(
    "INSERT INTO documents (content, embedding) VALUES (%s, %s::vector)",
    (text, str(emb)),
)
conn.commit()
conn.close()
print("✅ inserted 1 row")
