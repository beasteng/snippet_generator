"""23 — Paginated vector search with LIMIT/OFFSET."""
import os, psycopg
from openai import OpenAI

PAGE, PAGE_SIZE = 2, 5  # page 2, 5 per page

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="search term"
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT id, content
        FROM documents
        ORDER BY embedding <=> %s::vector
        LIMIT %s OFFSET %s
    """, (str(q_emb), PAGE_SIZE, (PAGE - 1) * PAGE_SIZE)).fetchall()

print(f"Page {PAGE}:", rows)
