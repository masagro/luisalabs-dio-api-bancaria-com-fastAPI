from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.utils import verificar_senha
from app.services.cliente_service import ClienteService

class AuthServices:

    @staticmethod
    async def autenticar(email: str, senha:str, db:AsyncSession):
        cliente = await ClienteService.buscar_por_email(email, db)

        if not cliente or not verificar_senha(senha, cliente.senha):
            raise HTTPException(status_code=400, detail="Credenciais Inválidas")
        
        return cliente