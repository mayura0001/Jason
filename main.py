import requests
import os
from dotenv import load_dotenv

load_dotenv()
print("successfully loaded env variables")

chats = []

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
    
    chats.append({"role": "user", "content": user_input})
    chats.append({"role": "assistant", "content": msg.get("content", "")})

    return {
        "reasoning": msg.get("reasoning", ""),
        "response": msg.get("content", "")
        
    }

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    full_input = "\n".join([f"{chat['role']}: {chat['content']}" for chat in chats]) + f"\nuser: {user_input}"
    result = send(full_input)
    print(f"Assistant: {result['response']}")
print(chats)
 