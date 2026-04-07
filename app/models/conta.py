from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base

class Contas(Base):
    __tablename__= "contas"

    id = Column(Integer, primary_key=True, index=True)
    numero_conta = Column(String, unique=True, nullable=False)
    saldo: Mapped[float] = mapped_column(default=0.00)
    cliente_id = Column(Integer, ForeignKey("clientes.id", ondelete="CASCADE"))

    cliente = relationship("Cliente", back_populates="contas")

    transacoes = relationship(
        "Transacoes",
        back_populates="conta",
        cascade="all, delete-orphan"
    )