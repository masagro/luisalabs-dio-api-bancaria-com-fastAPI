from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas.cliente import ClienteCreate, clienteRead
from app.services.cliente_service import ClienteService
from ..security import obter_usuario_atual
from app.models.cliente import Cliente

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.post("/", response_model=clienteRead, status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente: ClienteCreate, db: AsyncSession = Depends(get_session)):
    return await ClienteService.criar_cliente(data=cliente, db=db)

@router.get("/me", response_model=clienteRead)
async def ler_usuario_logado(cliente_atual: Cliente = Depends(obter_usuario_atual)):
    return cliente_atual
