"""
07 — Structured Output with Pydantic
======================================
Force the LLM to return validated JSON.
Interview point: Structured output prevents downstream parsing errors.
"""
from pydantic import BaseModel

class CityInfo(BaseModel):
    city: str
    country: str
    population_millions: float

def parse_llm_response(raw_json: str) -> CityInfo:
    """Validate raw LLM JSON against the schema."""
    return CityInfo.model_validate_json(raw_json)

if __name__ == "__main__":
    fake_llm_output = '{"city": "Paris", "country": "France", "population_millions": 2.1}'
    info = parse_llm_response(fake_llm_output)
    print(info)
    print(f"{info.city} has {info.population_millions}M people")
