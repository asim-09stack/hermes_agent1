import json
from datetime import datetime

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(entry):
    memory = load_memory()
    memory.append({
        "time": str(datetime.now()),
        "content": entry
    })
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)