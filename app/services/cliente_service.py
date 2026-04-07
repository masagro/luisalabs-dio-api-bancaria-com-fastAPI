from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate
from app.services.utils import gerar_hash

class ClienteService:

    @staticmethod
    async def criar_cliente(data: ClienteCreate, db: AsyncSession):
        # Verifica se o email já esta cadastrado
        stmt = select(Cliente).where(Cliente.email == data.email)
        resultado = await db.execute(stmt)
        existe = resultado.scalar_one_or_none()

        if existe:
            raise ValueError("Email já cadasatrado")

        novo_cliente = Cliente(
            nome = data.nome,
            email = data.email,
            senha = gerar_hash(data.senha)
        )

        db.add(novo_cliente)
        await db.commit()
        await db.refresh(novo_cliente)

        return novo_cliente
    
    @staticmethod
    async def buscar_por_email(email: str, db: AsyncSession):
        stmt = select(Cliente).where(Cliente.email == email)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    