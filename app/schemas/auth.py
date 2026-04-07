from pydantic import BaseModel, EmailStr

class LoginBase(BaseModel):
    email: EmailStr
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    