import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
print("successfully loaded env variables")

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "model": "openai/gpt-oss-120b:free",
        "messages": [
            {
                "role": "user",
                "content": "How many r's are in the word 'strawberry'?"
            }
        ],
        "reasoning": {"enabled": True}
    }
)

print(response.json()["choices"][0]["message"]["content"])
