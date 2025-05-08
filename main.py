from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI(
    title="Tech Challenge",
    version="0.0.1",
    description="Projeto do Tech Challenge Fiap"
)

# Banco de dados de usuários em memória
users = {
    "admin": "admin"
}

security = HTTPBasic()

def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username in users and username[username] == password:
        return username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Credenciais inválidas',
        headers={'WWW-Authenticate': "Basic"}
    )

@app.get("/")
async def home(username: str = Depends(verify_password)):
    return "Hello World"

@app.get("/producao")
async def home(username: str = Depends(verify_password)):
    return "Produção"

@app.get("/processamento")
async def home(username: str = Depends(verify_password)):
    return "Processamento"

@app.get("/comericalizacao")
async def home(username: str = Depends(verify_password)):
    return "Comercialização"

@app.get("/importacao")
async def home(username: str = Depends(verify_password)):
    return "Hello World"

@app.get("/exportacao")
async def home(username: str = Depends(verify_password)):
    return "Exportação"