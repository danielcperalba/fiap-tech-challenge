from sqlalchemy.orm import Session
from models import Producao, Processamento, Comercializacao, Importacao, Exportacao
#from .schemas import UserCreate

def get_producao(db: Session):
    return db.query(Producao).all()

def get_processamento(db: Session):
    return db.query(Processamento).all()

def get_comercializacao(db: Session):
    return db.query(Comercializacao).all()

def get_importacao(db: Session):
    return db.query(Importacao).all()

def get_exportacao(db: Session):
    return db.query(Exportacao).all()
