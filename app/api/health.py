from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.core.security import get_current_user
from app.models import ml
from pydantic import BaseModel, Field

router = APIRouter()

class FeaturesDict(BaseModel):
    data: dict[str, float] = Field(..., description="clave=nombre columna, valor=numérico")


@router.post("/predictions")
def make_prediction(body: FeaturesDict, current_user: str = Depends(get_current_user)):
    pred = ml.predict_from_dict(body.data)
    return {"user": current_user, "prediction": pred}
       