from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.conta import Contas
from app.schemas.conta import ContaCreate

class ContaService:
    @staticmethod
    async def criar_conta(data: ContaCreate, db: AsyncSession):
        #Verificar se o numero de conta já está cadastrado
        stmt = select(Contas).where(Contas.numero_conta == data.numero_conta)
        result = await db.execute(stmt)
        existe = result.scalar_one_or_none

        if existe:
            raise ValueError("Número de conta já esta em uso")
        
        nova_conta = Contas(
            numero_conta = data.numero_conta,
            cliente_id = data.cliente_id
        )

        db.add(nova_conta)
        await db.commit()
        await db.refresh(nova_conta)
        
        return nova_conta
    
    @staticmethod
    async def buscar_por_id(conta_id: int, db: AsyncSession):
        stmt = select(Contas).where(Contas.id == conta_id)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()