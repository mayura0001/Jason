import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Store conversation history
chat_history = []

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

MODEL = "openai/gpt-oss-120b:free"


def send_message(user_input: str) -> dict:
    """
    Sends user message to OpenRouter and returns assistant response.
    """

    # Build messages properly (chat history + new input)
    messages = chat_history + [
        {"role": "user", "content": user_input}
    ]

    payload = {
        "model": MODEL,
        "messages": messages,
        "reasoning": {"enabled": True}
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
    except requests.exceptions.RequestException as e:
        return {"response": f"Network error: {str(e)}", "reasoning": ""}

    # Handle bad HTTP responses
    if response.status_code != 200:
        return {
            "response": f"HTTP Error {response.status_code}: {response.text}",
            "reasoning": ""
        }

    data = response.json()

    # Safely extract message
    message = data.get("choices", [{}])[0].get("message", {})

    assistant_content = message.get("content", "")
    reasoning_content = message.get("reasoning", "")

    # Update history ONLY after successful response
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": assistant_content})

    return {
        "response": assistant_content,
        "reasoning": reasoning_content
    }


def chat_loop():
    print("Chat started (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            break

        if not user_input:
            continue

        result = send_message(user_input)

        print(f"\nAssistant: {result['response']}\n")


if __name__ == "__main__":
    chat_loop()
    print(chat_history)