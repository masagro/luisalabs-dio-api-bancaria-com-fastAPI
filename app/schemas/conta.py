from pydantic import BaseModel, Field

# Cadastra uma nova conta
class ContaCreate(BaseModel):
    cliente_id: int
    numero_conta: str = Field(...,min_length=3, max_length=20)


# Retorna dados da conta
class ContaRead(BaseModel):
    id: int
    numero_conta: str
    saldo: float
    cliente_id: int

    class Config:
        orm_mode = True