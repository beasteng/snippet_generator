"""20 — Full RAG pipeline: retrieve chunks → generate an answer with GPT."""
import os, psycopg
from openai import OpenAI

client   = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
question = "What are the benefits of vector databases?"

# Step 1: embed the question
q_emb = client.embeddings.create(
    model="text-embedding-3-small", input=question
).data[0].embedding

# Step 2: retrieve relevant chunks
with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    rows = conn.execute("""
        SELECT chunk_text FROM document_chunks
        ORDER BY embedding <=> %s::vector LIMIT 5
    """, (str(q_emb),)).fetchall()

context = "\n".join(r[0] for r in rows)

# Step 3: generate answer
answer = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Answer using ONLY the context below.\n\n" + context},
        {"role": "user",   "content": question},
    ],
).choices[0].message.content

print(f"Q: {question}\nA: {answer}")
