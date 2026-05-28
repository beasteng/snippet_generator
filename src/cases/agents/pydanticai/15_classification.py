"""15 — Text Classification: structured sentiment analysis."""
from pydantic import BaseModel
from pydantic_ai import Agent


class Sentiment(BaseModel):
    label: str   # e.g. "positive", "negative", "neutral"
    score: float  # 0.0–1.0


agent = Agent("openai:gpt-4o-mini", result_type=Sentiment)

print(agent.run_sync("Classify sentiment: 'I love this product!'").output)
