from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_accept_policy_accepted():
    response = client.post("/policy/", json={"cedula": "123456789", "confirm": True})
    assert response.status_code == 200
    assert response.json() == {"message": "Política aceptada"}

def test_accept_policy_rejected():
    response = client.post("/policy/", json={"cedula": "123456789", "confirm": False})
    assert response.status_code == 401
    assert response.json() == {"detail": "No acepta la política"}