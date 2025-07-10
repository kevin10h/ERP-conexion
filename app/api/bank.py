from fastapi import APIRouter, UploadFile, File, Depends
from app.core.security import get_current_user
from app.services.bank_client import send_payment

router = APIRouter()

@router.post("/transfer")
async def transfer(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    contents = await file.read()
    send_payment(contents, file.filename)
    return {"status": "sent", "filename": file.filename}
