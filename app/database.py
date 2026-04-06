from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "sqlite+aiosqlite:///./bank.db"

#criar engine assíncrona

engine = create_async_engine(
    DATABASE_URL,
    echo=True, 
)

# Criar sessão assíncrona

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

# Base para os modelso herdarem

Base = declarative_base()

#Dependencia para rotas

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
