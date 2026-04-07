from pydantic import BaseModel, Field, validator
from datetime import datetime

#Cadastra nova transação de saque ou deposito
class TransacaoCreate(BaseModel):
    tipo: str
    valor: float = Field(...,gt=0.01, description="O valor deve ser maior que zero(0)!") #gt=0 impede a inserção de valores menores que 0.01 (1 centavo)
    conta_id= int

    @validator("tipo") #Garante que as entradas apenas do tipo valido (saque ou deposito)
    def validar_tipo(cls, v):
        if v not in ["depostio", "saque"]:
            raise ValueError("Tipo deve ser 'depostio' ou 'saque'.")
        return v
    
#Retorna as transações vinculadas a conta

class TransacaoRead(BaseModel):
    id: int
    tipo: str
    valor:float
    data: datetime
    conta_id: int

    class Config:
        orm_mode = True
