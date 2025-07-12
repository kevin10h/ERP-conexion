from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Routers
from app.api import auth, health, bank, readings   #  ⬅️  añade readings aquí

# Infra / utilidades
from app.core.logging_config import init_logging
from app.db.session import engine
from app.db.base import Base

# NEW: registra los modelos para que SQLAlchemy los conozca
import app.db.models  # noqa: F401  (solo side-effect)

# --------------------------------------------------
init_logging()

app = FastAPI(title="ERP ↔ PivotConnect Bridge", version="1.0.0")
app.mount("/demo", StaticFiles(directory="app/static", html=True), name="demo")

# registra routers
app.include_router(auth.router,     prefix="/auth", tags=["auth"])
app.include_router(health.router,                 tags=["health"])
app.include_router(bank.router,      prefix="/bank", tags=["bank"])
app.include_router(readings.router,              tags=["readings"])

# crea tablas
Base.metadata.create_all(bind=engine)
