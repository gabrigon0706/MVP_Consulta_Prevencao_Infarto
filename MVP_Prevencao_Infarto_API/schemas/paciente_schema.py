from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """

    item1: int = 45 
    item2: int = 0
    item3: int = 231  
    item4: int = 85
    item5: int = 1 
    item6: int = 0 
    item7: int = 0  
    item8: int = 0  
    item9: int = 1  
    item10: int = 1  
    item11: int = 0  
    item12: int = 1
    item13: int = 2 
    item14: int = 729 
    item15: int = 6
    item16: int = 6  
    
    
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """

    id: int = 1
    item1: int = 45 
    item2: int = 0
    item3: int = 231  
    item4: int = 85
    item5: int = 1 
    item6: int = 0 
    item7: int = 0  
    item8: int = 0  
    item9: int = 1  
    item10: int = 1  
    item11: int = 0  
    item12: int = 1
    item13: int = 2 
    item14: int = 729 
    item15: int = 6
    item16: int = 6  
    outcome: int = None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no id do paciente.
    """
    id: int = 1

class PacienteIDBuscaSchema(BaseModel):
    """ Define como a busca de um paciente pelo ID deve ser representada.
    """
    id: int = 0

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para ser excluído será representado
    """
    id: int = "1"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "item1": paciente.item1,
        "item2": paciente.item2,
        "item3": paciente.item3,
        "item4": paciente.item4,
        "item5": paciente.item5,
        "item6": paciente.item6,
        "item7": paciente.item7,
        "item8": paciente.item8,
        "item9": paciente.item9,
        "item10": paciente.item10,
        "item11": paciente.item11,
        "item12": paciente.item12,
        "item13": paciente.item13,
        "item14": paciente.item14,
        "item15": paciente.item15,
        "item16": paciente.item16,
        "outcome": paciente.outcome
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
        "item1": paciente.item1,
        "item2": paciente.item2,
        "item3": paciente.item3,
        "item4": paciente.item4,
        "item5": paciente.item5,
        "item6": paciente.item6,
        "item7": paciente.item7,
        "item8": paciente.item8,
        "item9": paciente.item9,
        "item10": paciente.item10,
        "item11": paciente.item11,
        "item12": paciente.item12,
        "item13": paciente.item13,
        "item14": paciente.item14,
        "item15": paciente.item15,
        "item16": paciente.item16,
        "outcome": paciente.outcome
        })

    return {"pacientes": result}

class PacienteDelIdSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    id: int

class PacienteIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a exclusão do
    paciente pelo id.
    """
    id: int = 0
