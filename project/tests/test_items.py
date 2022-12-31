from fastapi.testclient import TestClient


def test_create_item(client: TestClient):
    response = client.post("/api/items/", json={"name": "Foo", "price": 42})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Foo", "price": 42}
