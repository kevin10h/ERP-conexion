"""
Inserta el usuario demo/demo (si no existe)
y varias lecturas de ejemplo.
"""
import random, time
from passlib.hash import bcrypt

# 👉  NUEVO: asegura que las tablas existen
from app.db.base import Base
from app.db.session import engine, SessionLocal
import app.db.models           # importa y registra User, Reading, etc.

from app.db.models import User, Reading

Base.metadata.create_all(bind=engine)   # crea las tablas si faltan

db = SessionLocal()

# ── usuario demo ───────────────────────────────────────────
usr = db.query(User).filter_by(username="demo").first()
if not usr:
    usr = User(username="demo",
               password_hash=bcrypt.hash("demo"))
    db.add(usr)
    db.flush()          # ← ahora usr.id existe

# ── lecturas de ejemplo ────────────────────────────────────
for _ in range(20):
    db.add(
        Reading(
            user_id=usr.id,
            heart_rate=random.randint(60, 90),
            spo2=random.randint(95, 100),
            respiration=random.randint(14, 20),
            ts=int(time.time()),
        )
    )

db.commit()
print("✔ Seed completado")
