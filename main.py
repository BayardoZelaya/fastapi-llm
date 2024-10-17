from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from langchain import LLMChain, PromptTemplate

app = FastAPI()

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

class Query(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(query: Query):
    # Define a prompt template
    prompt_template = PromptTemplate(template="Generate a response for: {prompt}", input_variables=["prompt"])
    
    # Create an LLMChain with the model and tokenizer
    llm_chain = LLMChain(model=model, tokenizer=tokenizer, prompt_template=prompt_template)
    
    # Generate text using the LLMChain
    generated_text = llm_chain.run(prompt=query.prompt)
    
    response = {"generated_text": generated_text}
    return response