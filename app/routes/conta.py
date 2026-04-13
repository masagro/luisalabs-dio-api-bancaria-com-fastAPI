from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas.conta import ContaCreate, ContaRead
from app.services.conta_service import ContaService
from app.security import obter_usuario_atual
from app.models.cliente import Cliente

router = APIRouter(prefix="/contas", tags=["contas"])

@router.post("/", response_model=ContaRead, status_code=status.HTTP_201_CREATED)
async def criar_conta(conta: ContaCreate, db: AsyncSession = Depends(get_session), usuario_atual: Cliente = Depends(obter_usuario_atual)):
    if conta.cliente_id != usuario_atual.id:
        raise HTTPException(status_code=403, detail="Você só pode criar contas para o seu próprio usuário.")
    return await ContaService.criar_conta(data=conta, db=db)

@router.get("/{conta_id}", response_model=ContaRead)
async def buscar_conta(conta_id: int, db: AsyncSession = Depends(get_session), usuario_atual: Cliente = Depends(obter_usuario_atual)):
    conta = await ContaService.buscar_por_id(conta_id=conta_id, db=db)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    if conta.cliente_id != usuario_atual.id:
        raise HTTPException(status_code=403, detail="Acesso negado à conta")
    return conta
