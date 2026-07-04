import requests
import json
from memory import load_memory, save_memory

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_agent(user_input):
    memory = load_memory()
    context = "\n".join([m["content"] for m in memory[-5:]])

    prompt = f"""
You are a persistent AI agent inspired by Hermes.
You remember past conversations.

Past memory:
{context}

User input:
{user_input}

Respond clearly.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": True
        },
        stream=True,
        timeout=120
    )

    output = ""

    for line in response.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line.decode())
            output += data.get("response", "")
        except json.JSONDecodeError:
            continue

    save_memory(f"User: {user_input}")
    save_memory(f"Agent: {output}")

    return output.strip() or "⚠️ No response generated."