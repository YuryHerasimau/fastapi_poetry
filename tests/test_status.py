from fastapi.testclient import TestClient
from fastapi_poetry.main import app
# from fastapi_poetry.settings import settings


def test_answer():
    client = TestClient(app)
    result = client.get('/status')
    assert result.status_code == 200
    assert result.json() == {'status': 'ok'}
    