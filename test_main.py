from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_create_todo():
    response = client.post("/todos", json={"id": "1", "title": "Test ToDo", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test ToDo"

def test_read_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_todo():
    response = client.put("/todos/1", json={"id": "1", "title": "Updated", "description": "Updated Description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"
    
def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"message": "ToDo deleted successfully"}