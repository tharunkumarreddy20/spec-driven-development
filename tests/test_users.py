from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users",
        json={"id": 1, "name": "Tharun", "email": "tharun@test.com"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Tharun"

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_duplicate_user_not_allowed():
    response = client.post(
        "/users",
        json={"id": 1, "name": "Duplicate", "email": "dup@test.com"}
    )
    assert response.status_code == 400