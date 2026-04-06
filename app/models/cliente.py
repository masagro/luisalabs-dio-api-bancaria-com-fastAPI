from sqlalchemy import Column, Integer, String
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)