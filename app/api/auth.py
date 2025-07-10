from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from app.core.security import create_token, verify_pw, hash_pw

router = APIRouter()

# Fake in-memory user store
_users = {"demo": hash_pw("demo")}

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    hashed = _users.get(form_data.username)
    if not hashed or not verify_pw(form_data.password, hashed):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Bad credentials")
    return {"access_token": create_token(form_data.username), "token_type": "bearer"}
