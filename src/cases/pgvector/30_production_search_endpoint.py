"""30 — Production-ready search with connection pooling, error handling, and caching."""
import os, hashlib, json, functools
from psycopg_pool import ConnectionPool
from openai import OpenAI

# --- Config ---------------------------------------------------------------
POOL = ConnectionPool(
    conninfo=os.environ["DATABASE_URL"],
    min_size=2, max_size=10, open=True,
)
CLIENT = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
MODEL  = "text-embedding-3-small"
TOP_K  = 10

# --- Embedding cache (simple in-memory, replace with Redis in prod) -------
@functools.lru_cache(maxsize=1024)
def get_embedding(text: str) -> list[float]:
    return CLIENT.embeddings.create(model=MODEL, input=text).data[0].embedding

# --- Search function ------------------------------------------------------
def semantic_search(
    query: str,
    tenant_id: str | None = None,
    threshold: float = 0.0,
    top_k: int = TOP_K,
) -> list[dict]:
    q_emb = get_embedding(query)
    q_str = str(q_emb)

    sql = """
        SELECT id, content, metadata,
               1 - (embedding <=> %s::vector) AS score
        FROM documents
        WHERE 1 - (embedding <=> %s::vector) >= %s
    """
    params: list = [q_str, q_str, threshold]

    if tenant_id:
        sql += " AND metadata->>'tenant_id' = %s"
        params.append(tenant_id)

    sql += " ORDER BY score DESC LIMIT %s"
    params.append(top_k)

    with POOL.connection() as conn:
        rows = conn.execute(sql, params).fetchall()

    return [
        {"id": r[0], "content": r[1], "metadata": r[2], "score": float(r[3])}
        for r in rows
    ]

# --- Demo -----------------------------------------------------------------
if __name__ == "__main__":
    results = semantic_search(
        "How do I integrate pgvector with Python?",
        tenant_id=None,
        threshold=0.3,
    )
    for r in results:
        print(f"[{r['score']:.4f}] id={r['id']}  {r['content'][:60]}")

    POOL.close()
    print("\n✅ pool closed")
