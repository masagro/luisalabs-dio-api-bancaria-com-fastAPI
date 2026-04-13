from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_session
from app.schemas.transacao import TransacaoCreate, TransacaoRead
from app.services.transacao_service import TransacaoService
from app.services.conta_service import ContaService
from app.security import obter_usuario_atual
from app.models.cliente import Cliente

router = APIRouter(prefix="/transacoes", tags=["transacoes"])

@router.post("/", response_model=TransacaoRead, status_code=status.HTTP_201_CREATED)
async def registrar_transacao(transacao: TransacaoCreate, db: AsyncSession = Depends(get_session), usuario_atual: Cliente = Depends(obter_usuario_atual)):
    conta = await ContaService.buscar_por_id(conta_id=transacao.conta_id, db=db)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    if conta.cliente_id != usuario_atual.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para transacionar nesta conta")
    
    try:
        return await TransacaoService.registrar_transacao(data=transacao, db=db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/extrato/{conta_id}", response_model=List[TransacaoRead])
async def obter_extrato(conta_id: int, db: AsyncSession = Depends(get_session), usuario_atual: Cliente = Depends(obter_usuario_atual)):
    conta = await ContaService.buscar_por_id(conta_id=conta_id, db=db)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    if conta.cliente_id != usuario_atual.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para ver o extrato desta conta")
    
    return await TransacaoService.extrato(conta_id=conta_id, db=db)
