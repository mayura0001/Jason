from urllib import response

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
print("successfully loaded env variables")


user_input = "Hello, how are you doing today?"

def send(user_input):
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
                    "content": user_input
                }
            ],
            "reasoning": {"enabled": True}
        }
    )

    if response.status_code != 200:
        return {"response": f"Error {response.status_code}", "reasoning": ""}

    msg = response.json()["choices"][0]["message"]
    return {
        "response": msg.get("content", ""),
        "reasoning": msg.get("reasoning", "")
    }




