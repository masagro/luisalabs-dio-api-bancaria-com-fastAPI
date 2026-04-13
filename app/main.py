from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.cliente import router as cliente_router
from app.routes.conta import router as conta_router
from app.routes.transacao import router as transacao_router

app = FastAPI(title="API Bancária", description="API para operações bancárias (Depósitos e Saques)", version="1.0.0")

app.include_router(auth_router)
app.include_router(cliente_router)
app.include_router(conta_router)
app.include_router(transacao_router)

@app.get("/")
async def root():
    return{"message": "API Bancaria Funcionando!"}
