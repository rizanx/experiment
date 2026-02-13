from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_ping():
    r = client.get("/ping")
    assert r.status_code == 200
    assert r.json() == {"message": "pong"}
