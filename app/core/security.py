import os, time, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette import status

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET = os.getenv("JWT_SECRET", "changeme")
ALGO = "HS256"
EXPIRES = 60 * 30  # 30 min

security_scheme = HTTPBearer()

def hash_pw(pw: str) -> str:
    return pwd_ctx.hash(pw)

def verify_pw(pw: str, hashed: str) -> bool:
    return pwd_ctx.verify(pw, hashed)

def create_token(sub: str) -> str:
    payload = {"sub": sub, "exp": time.time() + EXPIRES}
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def decode_token(token: str):
    return jwt.decode(token, SECRET, algorithms=[ALGO])

def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security_scheme)) -> str:
    try:
        payload = decode_token(creds.credentials)
        return payload["sub"]
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
