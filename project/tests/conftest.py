import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as _client:
        _client.headers.update({"X-API-Key": "password"})
        yield _client
