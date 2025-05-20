from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from typing import List
#Import dos códigos do banco de dados
from database import engine, get_db, Base, SessionLocal
import models
import schemas
#Import dos códigos de webscraping
from webscraping import ws_comercializacao, ws_exportacao, ws_importacao, ws_processamento, ws_producao

# CONFIGURAÇÕES

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tech Challenge",
    version="0.0.1",
    description="Projeto do Tech Challenge Fiap"
)

# Banco de dados de usuários em memória
users = {
    "admin": "admin",
}

security = HTTPBasic()

# Função que verifica se as credenciais estão corretas
def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    # Verifica se o nome do usuário e a senha estão certos
    if username in users and users[username] == password:
        return username # Retorna o nome de usuário se a autenticação for bem-sucedida
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Credenciais inválidas',
        headers={'WWW-Authenticate': "Basic"}
    )
        
# SALVANDO OS DADOS DO WEBSCRAPPING NO BANCO DE DADOS

# Comercialização
for item in ws_comercializacao.dados_comercializacao:
    
    # Verifica se os dados do arquivo estão corretos
    item_verificado = schemas.ComercializacaoCreate(
        produto=item[0], 
        quantidade=int(item[1].replace("-","0").replace(".",""))
        )
    
    # Cria o objeto
    db_item = models.Comercializacao(
        produto=item_verificado.produto,
        quantidade=item_verificado.quantidade
    )
    
    with SessionLocal() as db:
        db.add(db_item)
        db.commit() # Commit por item para pegar IntegrityError individualmente
        db.refresh(db_item) # Para obter o ID gerado e scraped_at

# Exportação
for item in ws_exportacao.dados_exportacao:
    
    # Verifica se os dados do arquivo estão corretos
    item_verificado = schemas.ExportacaoCreate(
        pais=item[0], 
        quantidade=int(item[1].replace("-","0").replace(".","")),
        valor=int(item[2].replace("-","0").replace(".",""))
        )
    
    # Cria o objeto
    db_item = models.Exportacao(
        pais=item_verificado.pais,
        quantidade=item_verificado.quantidade,
        valor=item_verificado.valor   
    )
    
    with SessionLocal() as db:
        db.add(db_item)
        db.commit() # Commit por item para pegar IntegrityError individualmente
        db.refresh(db_item) # Para obter o ID gerado e scraped_at
        
# Importação
for item in ws_importacao.dados_importacao:
    
    # Verifica se os dados do arquivo estão corretos
    item_verificado = schemas.ImportacaoCreate(
        pais=item[0], 
        quantidade=int(item[1].replace("-","0").replace(".","")),
        valor=int(item[2].replace("-","0").replace(".",""))
        )
    
    # Cria o objeto
    db_item = models.Importacao(
        pais=item_verificado.pais,
        quantidade=item_verificado.quantidade,
        valor=item_verificado.valor   
    )
    
    with SessionLocal() as db:
        db.add(db_item)
        db.commit() # Commit por item para pegar IntegrityError individualmente
        db.refresh(db_item) # Para obter o ID gerado e scraped_at

# Processamento
for item in ws_processamento.dados_processamento:
    
    # Verifica se os dados do arquivo estão corretos
    item_verificado = schemas.ProcessamentoCreate(
        cultivar=item[0], 
        quantidade=int(item[1].replace("-","0").replace(".","")),
        )
    
    # Cria o objeto
    db_item = models.Processamento(
        cultivar=item_verificado.cultivar,
        quantidade=item_verificado.quantidade,
    )
    
    with SessionLocal() as db:
        db.add(db_item)
        db.commit() # Commit por item para pegar IntegrityError individualmente
        db.refresh(db_item) # Para obter o ID gerado e scraped_at

# Produção
for item in ws_producao.dados_producao:    
    #Verifica se os dados do arquivo estão corretos
    item_verificado = schemas.ProducaoCreate(
        produto=item[0], 
        quantidade=int(item[1].replace("-","0").replace(".","")),
        )
    
    #Cria o objeto
    db_item = models.Producao(
        produto=item_verificado.produto,
        quantidade=item_verificado.quantidade,
    )
    
    with SessionLocal() as db:
        db.add(db_item)
        db.commit() # Commit por item para pegar IntegrityError individualmente
        db.refresh(db_item) # Para obter o ID gerado e scraped_at

# ENDPOINTS

@app.get("/")
async def home(username: str = Depends(verify_password)):
    return "Hello World"

@app.get("/producao", response_model=List[schemas.ProducaoBase], description="Retorna todos os dados de produção")
async def home(db: Session = Depends(get_db), username: str = Depends(verify_password)):
    # Cria a query que faz a consulta no banco de dados
    query = select(models.Producao)
    # Faz a consulta no banco de dados
    res = db.execute(query)
    # Retorna todos os objetos diretamente
    dados = res.scalars().all()
    return dados

@app.get("/processamento", response_model=List[schemas.ProcessamentoBase], description="Retorna todos os dados de processamento")
async def home(db: Session = Depends(get_db), username: str = Depends(verify_password)):
    # Cria a query que faz a consulta no banco de dados
    query = select(models.Processamento)
    # Faz a consulta no banco de dados
    res = db.execute(query)
    # Retorna todos os objetos diretamente
    dados = res.scalars().all()
    return dados

@app.get("/comericalizacao", response_model=List[schemas.ComercializacaoBase], description="Retorna todos os dados de comercialização")
async def home(db: Session = Depends(get_db), username: str = Depends(verify_password)):
    # Cria a query que faz a consulta no banco de dados
    query = select(models.Comercializacao)
    # Faz a consulta no banco de dados
    res = db.execute(query)
    # Retorna todos os objetos diretamente
    dados = res.scalars().all()
    return dados

@app.get("/importacao", response_model=List[schemas.ImportacaoBase], description="Retorna todos os dados de importação")
async def home(db: Session = Depends(get_db), username: str = Depends(verify_password)):
    # Cria a query que faz a consulta no banco de dados
    query = select(models.Importacao)
    # Faz a consulta no banco de dados
    res = db.execute(query)
    # Retorna todos os objetos diretamente
    dados = res.scalars().all()
    return dados

@app.get("/exportacao", response_model=List[schemas.ExportacaoBase], description="Retorna todos os dados de exportação")
async def home(db: Session = Depends(get_db), username: str = Depends(verify_password)):
       # Cria a query que faz a consulta no banco de dados
    query = select(models.Exportacao)
    # Faz a consulta no banco de dados
    res = db.execute(query)
    # Retorna todos os objetos diretamente
    dados = res.scalars().all()
    return dados