from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(query: Query):
    # Placeholder for LLM logic
    response = {"generated_text": f"Echo: {query.prompt}"}
    return response

