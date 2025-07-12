# app/crud/readings.py
from sqlalchemy.orm import Session
from app.db.models.reading import Reading      # ← ruta correcta

def get_readings_by_user(db: Session, user_id: int, limit: int = 20):
    return (
        db.query(Reading)
          .filter(Reading.user_id == user_id)
          .order_by(Reading.id.desc())
          .limit(limit)
          .all()
    )
