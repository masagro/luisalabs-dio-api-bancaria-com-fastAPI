from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_session
from app.services.auth_service import AuthServices
from app.security import criar_token_acesso

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    cliente = await AuthServices.autenticar(email=form_data.username, senha=form_data.password, db=db)
    
    access_token = criar_token_acesso(data={"sub": cliente.email})
    return {"access_token": access_token, "token_type": "bearer"}
