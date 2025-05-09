from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_query():
    response = client.post("/chat", data={"query": "What is AI?"})
    assert response.status_code == 200
    assert "response" in response.json()
