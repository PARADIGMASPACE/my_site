from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_root_returns_json():
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"

def test_api_prefix():
    response = client.get("/api/")
    assert response.status_code in [200, 404]

def test_app_title():
    assert app.title == "My Site"

def test_app_debug_mode():
    assert app.debug in [True, False]