from fastapi.testclient import TestClient


def test_category_create(client: TestClient):
    response = client.post('/categories/', json={
        'name': 'Categoria 1'
    })

    assert response.status_code == 201
    assert response.json()['id'] == 1


def test_category_update(client: TestClient):
    response = client.post('/categories/', json={
        'name': 'Categoria 1'
    })
    assert response.status_code == 201

    response = client.put(
        '/categories/1', json={'name': 'Categoria alterada'})

    assert response.status_code == 200
    assert response.json()['name'] == 'Categoria alterada'

    #response = client.get('/categories/1')
    #assert response.json()['name'] == 'Categoria alterada']

def test_category_delete(client: TestClient):
    response = client.get('/categories/', json={
        'name': 'Categoria 1'
    })
    assert response.status_code == 201

    response = client.delete(
        '/categories/1')

    assert response.status_code == 200
    assert response.json()['id'] == null
    #response = client.get('/categories/1')
    #assert response.json()['name'] == 'Categoria alterada']