from app.models.llm import generate_response

async def chat_with_bot(query: str):
    try:
        response = await generate_response(query)  # Ensure this is awaited
        return {"response": response}
    except Exception as e:
        return {"error": str(e), "response": "An error occurred while processing your request."}
