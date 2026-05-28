from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# 1. Point to your local LLM server
# For LM Studio, the default port is 1234
# For Ollama, you can append /v1 to your base_url if using the OpenAI wrapper
local_model = OpenAIModel(
    model_name="qwen2.5-7b-instruct",
    base_url="http://localhost:1234/v1",
    api_key="local" # API keys aren't required locally but the field must be populated
)

# 2. Define the schema you want the local model to return
class CityLocation(BaseModel):
    city: str
    country: str

# 3. Create the agent
agent = Agent(
    model=local_model,
    result_type=CityLocation,
    system_prompt="You are an expert geographer. Extract the city and country."
)

# 4. Run the agent
result = agent.run_sync("Where were the summer Olympics held in 2012?")

print(result.data)
