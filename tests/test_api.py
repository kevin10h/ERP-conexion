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
    payload = {"data":{
    "Age":20,"Gender":1,"Occupation":0,
    "Sleep Hours":8,"Physical Activity":4,
    "Caffeine Intake":150,"Alcohol Consumption":2,
    "Smoking":0,"Family History":0,"Stress Level":5,
    "Heart Rate":75,"Breathing Rate":18,"Sweating Level":2,
    "Dizziness":0,"Medication":0,"Therapy Sessions":0,
    "Major Event":1,"Diet Quality":3}}

    r = c.post("/predictions",json=payload,headers=headers)
    assert r.status_code==200 and r.json()["prediction"] in (0.0,1.0)

