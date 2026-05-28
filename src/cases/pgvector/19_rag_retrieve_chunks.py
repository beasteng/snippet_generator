"""19 — RAG pattern: retrieve the best chunks for a user question."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
question = "How does AI transform healthcare?"
q_emb = client.embeddings.create(
    model="text-embedding-3-small", input=question
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT doc_id, chunk_index, chunk_text,
               1 - (embedding <=> %s::vector) AS sim
        FROM document_chunks
        ORDER BY embedding <=> %s::vector
        LIMIT 5
    """, (str(q_emb), str(q_emb))).fetchall()

context = "\n---\n".join(r[2] for r in rows)
print("Retrieved context for RAG:\n", context[:500])
