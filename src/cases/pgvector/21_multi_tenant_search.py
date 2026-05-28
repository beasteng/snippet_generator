"""21 — Multi-tenant vector search with tenant_id filter."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="tenant-scoped query"
).data[0].embedding

TENANT = "tenant_42"

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT id, content
        FROM documents
        WHERE metadata->>'tenant_id' = %s
        ORDER BY embedding <=> %s::vector
        LIMIT 10
    """, (TENANT, str(q_emb))).fetchall()

print(f"Results for {TENANT}:", rows)
