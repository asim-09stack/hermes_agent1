from fastapi import FastAPI
from agent import run_agent

app = FastAPI(title="Hermes-style AI Agent")

@app.post("/chat")
def chat(message: str):
    reply = run_agent(message)
    return {"response": reply}