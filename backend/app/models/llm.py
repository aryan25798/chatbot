import openai
import os
from dotenv import load_dotenv
from fastapi import HTTPException

# Load environment variables
load_dotenv()

# Get OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key if it exists
if openai_api_key:
    openai.api_key = openai_api_key
else:
    openai.api_key = None

def generate_response(query: str):
    if not openai_api_key:
        # Raise HTTPException for API key not being set
        raise HTTPException(
            status_code=400,
            detail="Sorry, the OpenAI API key is not configured. Please set it up and try again."
        )

    try:
        # Generate response using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query}],
        )
        return response.choices[0].message["content"]
    except Exception as e:
        # Return error message if the API call fails
        raise HTTPException(status_code=500, detail=f"Error generating response: {e}")
