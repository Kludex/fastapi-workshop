import pytest
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as _client:
        yield _client
