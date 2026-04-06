from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False) #senha criptografada

    contas = relationship(
        "Contas",
        back_populates="cliente",
        cascade="all, delete-orphan"
    )