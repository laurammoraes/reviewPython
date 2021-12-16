from fastapi.testclient import TestClient


def test_customer_create(client: TestClient):
    response = client.post('/customers/', json={
        'firstName': 'Laura'
    })

    assert response.status_code == 201
    assert response.json()['id'] == 1


def test_customer_update(client: TestClient):
    response = client.post('/customers/', json={
        'firstName': 'Laura'
    })
    assert response.status_code == 201

    response = client.put(
        '/customers/1', json={'firstName': 'Eva'})

    assert response.status_code == 200
    assert response.json()['firstName'] == 'Eva'

   