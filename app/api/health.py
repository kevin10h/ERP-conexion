from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.core.security import get_current_user
from app.models import ml

router = APIRouter()

class Features(BaseModel):
    features: list[float] = Field(..., description="Numeric feature vector")

@router.get("/readings")
def root_readings(current_user: str = Depends(get_current_user)):
    """Dummy endpoint returning fixed health readings"""
    return {"user": current_user, "heart_rate": 72, "blood_pressure": "120/80"}

@router.post("/predictions")
def make_prediction(data: Features, current_user: str = Depends(get_current_user)):
    pred = ml.predict(data.features)
    return {"user": current_user, "prediction": pred}
