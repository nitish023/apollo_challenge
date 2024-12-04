import pytest
from app import db, app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_vehicles(client):
    response = client.get("/vehicle")
    assert response.status_code == 200
    assert response.json == []

def test_create_vehicle(client):
    sample_vehicle = {
        "vin": "1HGCM82633A123456",
        "manufacturer_name": "Honda",
        "description": "Sedan",
        "horse_power": 150,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 25000.00,
        "fuel_type": "Gasoline"
    }
    response = client.post('/vehicle', json=sample_vehicle)
    assert response.status_code == 201
    assert response.json['vin'] ==  "1HGCM82633A123456"
    assert response.json['manufacturer_name'] == "Honda"

def test_get_vehicle_by_vin(client):
    client.post('/vehicle', json={
        "vin": "1HGCM82633A123456",
        "manufacturer_name": "Honda",
        "description": "Sedan",
        "horse_power": 150,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 25000.00,
        "fuel_type": "Gasoline"
    })
    response = client.get('/vehicle/1HGCM82633A123456')
    assert response.status_code == 200
    assert response.json['vin'] == '1HGCM82633A123456'

def test_update_vehicle(client):
    client.post('/vehicle', json={
        "vin": "1HGCM82633A123456",
        "manufacturer_name": "Honda",
        "description": "Sedan",
        "horse_power": 150,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 25000.00,
        "fuel_type": "Gasoline"
    })   
    response = client.put('/vehicle/1HGCM82633A123456', json={
        "horse_power": 180,
        "description": "Updated Sedan"
    })
    assert response.status_code == 200
    assert response.json['horse_power'] == 180
    assert response.json['description'] == "Updated Sedan"

def test_delete_vehicle(client):
    client.post('/vehicle', json={
        "vin": "1HGCM82633A123456",
        "manufacturer_name": "Honda",
        "description": "Sedan",
        "horse_power": 150,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 25000.00,
        "fuel_type": "Gasoline"
    })   
    response = client.delete('/vehicle/1HGCM82633A123456')
    assert response.status_code == 204
    response = client.get('/vehicle/1HGCM82633A123456')
    assert response.status_code == 404

def test_invalid_json(client):
    response = client.post('/vehicle', data="Invalid JSON")
    assert response.status_code == 400
    assert response.json == {'error': 'Bad Request'}

def test_missing_required_fields(client):
    response = client.post('/vehicle', json={
        "vin": "1HGCM82633A123456"
    })
    assert response.status_code == 422
    assert response.json == {'error': 'Unprocessable Entry'}
