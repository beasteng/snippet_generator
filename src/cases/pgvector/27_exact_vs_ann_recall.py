"""27 — Compare exact (seq-scan) vs ANN (index) recall."""
import os, psycopg
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
q_emb  = client.embeddings.create(
    model="text-embedding-3-small", input="recall benchmark"
).data[0].embedding
q_str  = str(q_emb)

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    # Exact search (force seq-scan)
    conn.execute("SET enable_indexscan = off; SET enable_bitmapscan = off;")
    exact = {r[0] for r in conn.execute(
        "SELECT id FROM documents ORDER BY embedding <=> %s::vector LIMIT 10", (q_str,)
    )}

    # ANN search (use index)
    conn.execute("RESET enable_indexscan; RESET enable_bitmapscan;")
    ann = {r[0] for r in conn.execute(
        "SELECT id FROM documents ORDER BY embedding <=> %s::vector LIMIT 10", (q_str,)
    )}

recall = len(exact & ann) / len(exact) if exact else 0
print(f"Recall@10 = {recall:.0%}  (exact={exact}, ann={ann})")
