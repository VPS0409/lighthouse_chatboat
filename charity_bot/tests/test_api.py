# tests/test_api.py
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ask_endpoint(client):
    response = client.post('/api/ask', json={'question': 'Как получить коляску?'})
    assert response.status_code == 200