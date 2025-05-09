from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ingest_url():
    response = client.post("/ingest", data={"url": "https://example.com"})
    assert response.status_code == 200
    assert response.json()["status"] == "Content ingested"
