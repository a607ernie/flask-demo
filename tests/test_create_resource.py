def test_create_resource(client):
    response = client.post('/api/v1/resource', json={'key': 'value'})
    assert response.status_code == 201
    assert response.get_json() == {'resource': {'key': 'value'}}