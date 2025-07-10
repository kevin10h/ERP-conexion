from fastapi import FastAPI
from app.api import auth, health, bank
from app.core.logging_config import init_logging

init_logging()
app = FastAPI(title="ERP ↔ PivotConnect Bridge", version="1.0.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(health.router, tags=["health"])
app.include_router(bank.router, prefix="/bank", tags=["bank"])
