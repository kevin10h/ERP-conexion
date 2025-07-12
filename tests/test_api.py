from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def _token():
    r = client.post('/auth/token', data={'username': 'demo', 'password': 'demo'})
    return r.json()['access_token']

def test_predict_json():
    c = TestClient(app)
    tok = c.post("/auth/token", data={'username':'demo','password':'demo'}).json()['access_token']
    headers = {'Authorization':f'Bearer {tok}'}
    payload = {"data":{"Age":20,"Gender":1,"Occupation":0,"Sleep":8,"Physical":4,
                       "Caffeine":150,"Alcohol":2,"Smoking":0,"Family":0,"Stress":5,
                       "Heart":75,"Breathing":18,"Sweating":2,"Dizziness":0,"Medication":0,
                       "Therapy":0,"Major":1,"Diet":3}}
    r = c.post("/predictions",json=payload,headers=headers)
    assert r.status_code==200 and r.json()["prediction"] in (0.0,1.0)

