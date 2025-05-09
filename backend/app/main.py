from fastapi import FastAPI, Form, UploadFile, HTTPException
from backend.app.ingest import ingest_content
from backend.app.chat import chat_with_bot
from backend.app.models.embeddings import embedding_model

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Chatbot API"}

@app.post("/ingest")
async def ingest(url: str = Form(None), file: UploadFile = None):
    return await ingest_content(url, file)

@app.post("/chat")
async def chat(query: str = Form(...)):
    if embedding_model is None:
        raise HTTPException(status_code=400, detail="OpenAI API key is not configured. Please set the API key.")

    # Proceed with normal bot interaction if the API key is configured
    return await chat_with_bot(query)
