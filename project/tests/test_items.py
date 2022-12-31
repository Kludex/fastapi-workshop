from fastapi.testclient import TestClient


def test_create_item(client: TestClient):
    response = client.post("/api/items/", json={"name": "Foo", "price": 42})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Foo", "price": 42}


def test_get_item(client: TestClient):
    client.post("/api/items/", json={"name": "Foo", "price": 42})
    response = client.get("/api/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Foo", "price": 42}


def test_get_items(client: TestClient):
    client.post("/api/items/", json={"name": "Foo", "price": 42})
    client.post("/api/items/", json={"name": "Bar", "price": 42})
    response = client.get("/api/items/")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Foo", "price": 42},
        {"id": 2, "name": "Bar", "price": 42},
    ]


def test_delete_item(client: TestClient):
    client.post("/api/items/", json={"name": "Foo", "price": 42})
    response = client.delete("/api/items/1")
    assert response.status_code == 204
