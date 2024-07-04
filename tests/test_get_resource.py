def test_get_resource(client):
    response = client.get('/api/v1/resource')
    assert response.status_code == 200
    assert response.get_json() == {'resource': 'This is a resource'}