"""28 — Item-to-item recommendation: find documents similar to doc #1."""
import os, psycopg

SEED_ID = 1

with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
    # Fetch the seed item's embedding
    seed = conn.execute(
        "SELECT embedding FROM documents WHERE id = %s", (SEED_ID,)
    ).fetchone()
    if not seed:
        raise ValueError(f"Document {SEED_ID} not found")

    # Find similar (exclude self)
    rows = conn.execute("""
        SELECT id, content,
               1 - (embedding <=> %s) AS sim
        FROM documents
        WHERE id != %s
        ORDER BY embedding <=> %s
        LIMIT 5
    """, (seed[0], SEED_ID, seed[0])).fetchall()

print(f"Documents similar to id={SEED_ID}:")
for r in rows:
    print(f"  id={r[0]}  sim={r[2]:.4f}  {r[1][:60]}")
