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
    "Age": 20,
    "Gender": 1,
    "Occupation": 0,
    "Sleep Hours": 8,
    "Physical Activity (hrs/week)": 4,
    "Caffeine Intake (mg/day)": 150,
    "Alcohol Consumption (drinks/week)": 2,
    "Smoking": 0,
    "Family History of Anxiety": 0,
    "Stress Level (1-10)": 5,
    "Heart Rate (bpm)": 75,
    "Breathing Rate (breaths/min)": 18,
    "Sweating Level (1-5)": 2,
    "Dizziness": 0,
    "Medication": 0,
    "Therapy Sessions (per month)": 0,
    "Recent Major Life Event": 1,
    "Diet Quality (1-10)": 3
    }}

    r = c.post("/predictions",json=payload,headers=headers)
    assert r.status_code==200 and r.json()["prediction"] in (0.0,1.0)

