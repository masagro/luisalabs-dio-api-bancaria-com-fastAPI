from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Transacao(Base):
    __tablename__ = "transacoes"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False) #Saque ou Deposito
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)

    conta_id = Column(Integer, ForeignKey("contas.id", ondelete="CASCADE"))
    conta = relationship("Contas", back_populates="transacoes")