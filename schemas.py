from pydantic import BaseModel

# Esquemas para validação dos dados

# PRODUÇÃO

class ProducaoBase(BaseModel):
    produto: str
    quantidade: float
    
class ProducaoCreate(ProducaoBase):
    pass

# PROCESSAMENTO
        
class ProcessamentoBase(BaseModel):
    cultivar: str
    quantidade: float
    
class ProcessamentoCreate(ProcessamentoBase):
    pass

# COMERCIALIZAÇÃO
    
class ComercializacaoBase(BaseModel):
    produto: str
    quantidade: float
    
class ComercializacaoCreate(ComercializacaoBase):
    pass
   
# IMPORTAÇÃO
     
class ImportacaoBase(BaseModel):
    pais: str
    quantidade: int
    valor: float

class ImportacaoCreate(ImportacaoBase):
    pass
        
# EXPORTAÇÃO

class ExportacaoBase(BaseModel):
    pais: str
    quantidade: int
    valor: float

class ExportacaoCreate(ExportacaoBase):
    pass
        