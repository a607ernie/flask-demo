def test_delete_resource(client):
    response = client.delete('/api/v1/resource/1')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Resource 1 deleted'}
