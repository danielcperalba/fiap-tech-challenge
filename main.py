from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from crud import get_producao, get_processamento, get_comercializacao, get_importacao, get_exportacao
from models import Producao, Processamento, Comercializacao, Importacao, Exportacao
from schemas import ProducaoResponse, ProcessamentoResponse, ComercializacaoResponse, ImportacaoResponse, ExportacaoResponse

Base.metadata.create_all(bind=engine)

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
    producao = get_producao()
    return producao

@app.get("/processamento")
async def home(username: str = Depends(verify_password)):
    processamento = get_processamento()
    return processamento

@app.get("/comericalizacao")
async def home(username: str = Depends(verify_password)):
    comercializacao = get_comercializacao()
    return comercializacao

@app.get("/importacao")
async def home(username: str = Depends(verify_password)):
    importacao = get_importacao()
    return importacao

@app.get("/exportacao")
async def home(username: str = Depends(verify_password)):
    exportacao = get_exportacao()
    return exportacao