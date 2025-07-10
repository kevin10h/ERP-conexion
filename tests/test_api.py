from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def _token():
    r = client.post('/auth/token', data={'username': 'demo', 'password': 'demo'})
    return r.json()['access_token']

def test_prediction():
    t = _token()
    r = client.post('/predictions', headers={'Authorization': f'Bearer {t}'}, json={'features':[0.1,0.2,0.3]})
    assert r.status_code == 200
    assert 'prediction' in r.json()
