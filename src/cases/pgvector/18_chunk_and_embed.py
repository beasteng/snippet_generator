"""18 — Split a long document into chunks, embed, and store each."""
import os, psycopg
from openai import OpenAI

def chunk_text(text: str, max_tokens: int = 300) -> list[str]:
    words = text.split()
    chunks, current = [], []
    for w in words:
        current.append(w)
        if len(current) >= max_tokens:
            chunks.append(" ".join(current))
            current = []
    if current:
        chunks.append(" ".join(current))
    return chunks

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
long_text = "Artificial intelligence is transforming every industry. " * 200

chunks = chunk_text(long_text)
embs   = client.embeddings.create(
    model="text-embedding-3-small", input=chunks
).data

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS document_chunks (
            id          bigserial PRIMARY KEY,
            doc_id      bigint NOT NULL,
            chunk_index int NOT NULL,
            chunk_text  text NOT NULL,
            embedding   vector(1536) NOT NULL
        );
    """)
    for i, (chunk, item) in enumerate(zip(chunks, embs)):
        conn.execute(
            "INSERT INTO document_chunks (doc_id, chunk_index, chunk_text, embedding) "
            "VALUES (%s, %s, %s, %s::vector)",
            (1, i, chunk, str(item.embedding)),
        )
    conn.commit()
print(f"✅ stored {len(chunks)} chunks")
