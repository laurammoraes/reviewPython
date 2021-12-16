from fastapi.testclient import TestClient


def test_coupon_create(client: TestClient):
    response = client.post('/coupons/', json={
        'code': '123'
    })

    assert response.status_code == 201
    assert response.json()['id'] == 1


def test_coupon_update(client: TestClient):
    response = client.post('/coupons/', json={
        'code': '123'
    })
    assert response.status_code == 201

    response = client.put(
        '/coupons/1', json={'code': '123'})

    assert response.status_code == 200
    assert response.json()['code'] == '123'

   