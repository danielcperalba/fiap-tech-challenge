from pydantic import BaseModel
class ProducaoResponse(BaseModel):
    id: int
    produto: str
    quantidade: float
        
class ProcessamentoResponse(BaseModel):
    id: int
    cultivar: str
    quantidade: float
        
class ComercializacaoResponse(BaseModel):
    id: int
    produto: str
    quantidade: float
        
class ImportacaoResponse(BaseModel):
    id: int
    pais: str
    quantidade: int
    valor: float
        
class ExportacaoResponse(BaseModel):
    id: int
    pais: str
    quantidade: int
    valor: float
        