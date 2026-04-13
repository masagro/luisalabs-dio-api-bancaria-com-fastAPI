from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.transacao import Transacao
from app.models.conta import Contas
from app.schemas.transacao import TransacaoCreate

class TransacaoService:
    @staticmethod
    async def registrar_transacao(data: TransacaoCreate, db: AsyncSession):
        #Busca a conta no banco de dados
        stmt = select(Contas).where(Contas.id == data.conta_id)
        result = await db.execute(stmt)
        conta = result.scalar_one_or_none()

        if not conta:
            raise ValueError("Conta não encontrada")
        
        #Validação do saque
        if data.tipo == "saque" and conta.saldo < data.valor:
            raise ValueError ("Saldo Insuficiente")
        
        #Atualização do saldo
        if data.tipo == "deposito":
            conta.saldo += data.valor
        else:
            conta.saldo -= data.valor

        trans = Transacao(
            tipo = data.tipo,
            valor = data.valor,
            conta_id = data.conta_id
        )

        db.add(trans)
        await db.commit()
        await db.refresh(trans)
        await db.refresh(conta)

        return trans
    
    @staticmethod
    async def extrato(conta_id: int, db: AsyncSession):
        stmt = select(Transacao).where(Transacao.conta_id == conta_id)
        result = await db.execute(stmt)
        return result.scalars().all()
