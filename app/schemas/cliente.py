from pydantic import BaseModel, EmailStr, Field


# Cadasatro de novo cliente
class ClienteCreate(BaseModel):
    nome: str = Field(...,min_length=3, max_length=100)
    email: EmailStr
    senha: str = Field(...,max_length=6)

# Retorna dados do cliente sem exibir senha
class clienteRead(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        orm_mode = True #permite retornar objetos SQLAlchemy
