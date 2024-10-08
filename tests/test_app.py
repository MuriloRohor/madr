from http import HTTPStatus

from fastapi.testclient import TestClient

from madr.app import app


def test_read_root_return_ok():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
