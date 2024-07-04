def test_update_resource(client):
    response = client.put('/api/v1/resource/1', json={'key': 'new_value'})
    assert response.status_code == 200
    assert response.get_json() == {'resource': 'Updated resource 1 with data {\'key\': \'new_value\'}'}