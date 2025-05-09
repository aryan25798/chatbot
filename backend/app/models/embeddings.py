import os
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from fastapi import HTTPException

# Load environment variables from a .env file
load_dotenv()

# Get OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize embedding model only if the API key is available
if openai_api_key:
    embedding_model = OpenAIEmbeddings(openai_api_key=openai_api_key)
else:
    embedding_model = None  # Placeholder if no API key is present

# Load or initialize vector store (FAISS)
vector_store = FAISS.load_local("vectorstore") if os.path.exists("vectorstore") else FAISS()

def index_content(content: str):
    if not embedding_model:
        raise HTTPException(status_code=400, detail="OpenAI API key is not configured. Cannot index content at this moment.")

    try:
        # Add content to the FAISS vector store
        vector_store.add_texts([content], embedding_model)
        # Save the updated vector store
        vector_store.save_local("vectorstore")
        return "Content indexed successfully."
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error indexing content: {e}")
