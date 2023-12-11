from sqlalchemy import Column, String, Integer
from model import Base

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    item1 = Column("Idade", Integer)
    item2 = Column("Sexo", Integer)
    item3 = Column("Colesterol", Integer)
    item4 = Column("Batimento cardíaco", Integer)
    item5 = Column("Diabetes", Integer)
    item6 = Column("Histórico na família", Integer)
    item7 = Column("Fumante", Integer)
    item8 = Column("Obesidade", Integer)
    item9 = Column("Consumo de álcool", Integer)
    item10 = Column("Dieta", Integer)
    item11 = Column("Problema cardíaco", Integer)
    item12 = Column("Uso de medicação", Integer)
    item13 = Column("Nível de estresse", Integer)
    item14 = Column("Triglicerídeos", Integer)
    item15 = Column("Atividade física na semana", Integer)
    item16 = Column("Horas de sono", Integer)
    outcome = Column("Diagnostic", Integer, nullable=True)
    
    def __init__(self, item1:int, item2:int, item3:int, item4:int,
                 item5:int, item6:int, item7:int, 
                 item8:int, item9:int, item10:int, item11:int, 
                 item12:int, item13:int, item14:int, item15:int, item16:int, outcome:int, 
                 ):
        """
        Cria um Paciente

        Arguments:
        item1 = Idade
        item2 = Sexo
        item3 = Colesterol
        item4 = Batimento cardíaco
        item5 = Diabetes
        item6 = Histórico na família
        item7 = Fumante
        item8 = Obesidade
        item9 = Consumo de álcool
        item10 = Dieta
        item11 = Problema cardíaco
        item12 = Uso de medicação
        item13 = Nível de estresse
        item14 = Triglicerídeos
        item15 = Atividade física na semana
        item16 = Horas de sono
        outcome = Diagnóstico
        """
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        self.item6 = item6
        self.item7 = item7
        self.item8 = item8
        self.item9 = item9
        self.item10 = item10
        self.item11 = item11
        self.item12 = item12
        self.item13 = item13
        self.item14 = item14
        self.item15 = item15
        self.item16 = item16
        self.outcome = outcome