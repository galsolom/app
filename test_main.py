from fastapi.testclient import TestClient
import os

from app.main import app

client = TestClient(app)


def test_a():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_b():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}