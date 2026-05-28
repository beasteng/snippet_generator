"""16 — Re-embed and UPDATE after document content changes."""
import os, psycopg
from openai import OpenAI

DOC_ID   = 1
new_text = "completely rewritten document content"

client  = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
new_emb = client.embeddings.create(
    model="text-embedding-3-small", input=new_text
).data[0].embedding

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    conn.execute(
        "UPDATE documents SET content=%s, embedding=%s::vector WHERE id=%s",
        (new_text, str(new_emb), DOC_ID),
    )
    conn.commit()
print(f"✅ updated doc {DOC_ID}")
