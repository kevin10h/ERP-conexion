from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_current_user        # <- importa solo la función
from app.db.session import SessionLocal
from app.db.models.user import User
from app.crud.readings import get_readings_by_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/readings")
def list_readings(
    db: Session = Depends(get_db),
    current_username: str = Depends(get_current_user)   # ← **recibe un str**
):
    # 1️⃣ Buscar la instancia User por username
    user = db.query(User).filter_by(username=current_username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # 2️⃣ Obtener lecturas
    rows = get_readings_by_user(db, user.id)
    return [
        {
            "heart_rate":  r.heart_rate,
            "spo2":        r.spo2,
            "respiration": r.respiration,
        }
        for r in rows
    ]
