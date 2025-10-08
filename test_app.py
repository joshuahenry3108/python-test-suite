import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# def test_api_returns_hello_message(client):
#     response = client.get("/api")
#     assert response.status_code == 200
#     assert response.is_json
#     data = response.get_json()
#     assert data == {"message": "Hello from Flask!"}

def test_failure_example():
    assert False, "This test is supposed to fail"