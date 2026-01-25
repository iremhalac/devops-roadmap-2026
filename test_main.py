from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "OK"

def test_predict_basic():
    resp = client.post("/predict", json={"feature1": 2.0, "feature2": 3.0})
    assert resp.status_code == 200
    data = resp.json()
    assert "prediction" in data
