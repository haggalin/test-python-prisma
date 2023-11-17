from fastapi.testclient import TestClient
from app.main import app


def test_create_user():
    with TestClient(app) as client:
        res = client.post('/user', json={'username': 'test-bingo'})
        assert res.status_code == 200
        assert 'id' in res.json()
