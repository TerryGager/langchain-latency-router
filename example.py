import requests
from langchain.chat_models import ChatOpenAI

# Get the fastest provider
res = requests.get("https://inferenceLatency.com/api/fastest")
fastest = res.json().get("provider")

# Map provider to LangChain model
provider_model_map = {
    "openai": "gpt-4",
    "anthropic": "claude-3-haiku-20240307",
    "mistral": "mistral-large-latest",
}
model_name = provider_model_map.get(fastest, "gpt-4")

# Run with LangChain
llm = ChatOpenAI(model_name=model_name)
response = llm.invoke("What's the capital of Japan?")
print(response)
