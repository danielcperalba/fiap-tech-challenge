from sqlalchemy import Column, Integer, String, Float
from database import Base

# Modelos das tabelas do banco de dados

class Producao(Base):
    __tablename__ = "producao"
    
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String, index=True)
    quantidade = Column(Float, index=True)
    
class Processamento(Base):
    __tablename__ = "processamento"
    
    id = Column(Integer, primary_key=True, index=True)
    cultivar = Column(String, index=True)
    quantidade = Column(Float, index=True)
    
class Comercializacao(Base):
    __tablename__ = "comercializacao"
    
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String, index=True)
    quantidade = Column(Float, index=True)
    
class Importacao(Base):
    __tablename__ = "importacao"
    
    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String, index=True)
    quantidade = Column(Integer, index=True)
    valor = Column(Float, index=True)

class Exportacao(Base):
    __tablename__ = "exportacao"
    
    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String, index=True)
    quantidade = Column(Integer, index=True)
    valor = Column(Float, index=True)