import pytest
from app.run import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# def test_home(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.get_json() == {'message': 'Welcome to the Flask API!'}

def test_get_resource(client):
    response = client.get('/api/v1/resource')
    assert response.status_code == 200
    assert response.get_json() == {'resource': 'This is a resource'}

def test_create_resource(client):
    response = client.post('/api/v1/resource', json={'key': 'value'})
    assert response.status_code == 201
    assert response.get_json() == {'resource': {'key': 'value'}}

def test_update_resource(client):
    response = client.put('/api/v1/resource/1', json={'key': 'new_value'})
    assert response.status_code == 200
    assert response.get_json() == {'resource': 'Updated resource 1 with data {\'key\': \'new_value\'}'}

def test_delete_resource(client):
    response = client.delete('/api/v1/resource/1')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Resource 1 deleted'}
