"""25 — Async embedding generation and async DB insert."""
import os, asyncio
import psycopg
from openai import AsyncOpenAI

async def main():
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
    texts  = ["async text one", "async text two", "async text three"]

    resp = await client.embeddings.create(
        model="text-embedding-3-small", input=texts
    )

    aconn = await psycopg.AsyncConnection.connect(os.environ["DATABASE_URL"])
    async with aconn:
        for text, item in zip(texts, resp.data):
            await aconn.execute(
                "INSERT INTO documents (content, embedding) VALUES (%s, %s::vector)",
                (text, str(item.embedding)),
            )
        await aconn.commit()
    print(f"✅ async-inserted {len(texts)} rows")

asyncio.run(main())
