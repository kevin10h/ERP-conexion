import os
from functools import lru_cache

class Settings:
    JWT_SECRET: str = os.getenv("JWT_SECRET", "changeme")
    MODEL_PATH: str = os.getenv("MODEL_PATH", "")
    BANK_HOST: str = os.getenv("BANK_HOST", "localhost")
    BANK_PORT: int = int(os.getenv("BANK_PORT", 2222))
    BANK_USER: str = os.getenv("BANK_USER", "pivot_user")
    BANK_KEY: str = os.getenv("BANK_KEY", "pivot_user.ppk")

@lru_cache
def get_settings():
    return Settings()
