from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from model import Session, Paciente, Model
from logger import logger
from schemas import *
from flask_cors import CORS
import logging
import numpy as np

info = Info(title="API Prevenção a Infarto", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação Swagger", description="Documentação estilo Swagger.")
paciente_tag = Tag(name="Paciente", description="Adição, visualização e remoção de pacientes na base de dados.")


def home():
    """Redireciona para documentação da API no estilo Swagger.
    """
    return redirect('/openapi/swagger')

# Rota de busca de todos os pacientes
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Retorna uma lista de pacientes cadastrados na base.
    """
    session = Session()
    
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        logger.warning("Não há pacientes cadastrados na base :/")
        return {"message": "Não há pacientes cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d pacientes econtrados" % len(pacientes))
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def adicionar_paciente(form: PacienteSchema):
    """Faz a adição de um novo paciente na base de dados.
    """
    # Carregando modelo e scaler
    ml_path = 'ml_model/modelo_naive_bayes.pkl'
    scaler_path = 'ml_model/scaler.pkl'
    modelo, scaler = Model.carrega_modelo(ml_path, scaler_path)

    # Normalizando os dados do formulário com o StandardScaler
    normalized_data = scaler.transform([[
        form.item1, form.item2, form.item3, form.item4,
        form.item5, form.item6, form.item7, form.item8,
        form.item9, form.item10, form.item11, form.item12,
        form.item13, form.item14, form.item15, form.item16
    ]])

    # Realizando a predição
    outcome = Model.preditor(modelo, scaler, normalized_data[0])  # Acessando os elementos do array

    novo_paciente = Paciente(
        item1=float(normalized_data[0][0]),
        item2=float(normalized_data[0][1]),
        item3=float(normalized_data[0][2]),
        item4=float(normalized_data[0][3]),
        item5=float(normalized_data[0][4]),
        item6=float(normalized_data[0][5]),
        item7=float(normalized_data[0][6]),
        item8=float(normalized_data[0][7]),
        item9=float(normalized_data[0][8]),
        item10=float(normalized_data[0][9]),
        item11=float(normalized_data[0][10]),
        item12=float(normalized_data[0][11]),
        item13=float(normalized_data[0][12]),
        item14=float(normalized_data[0][13]),
        item15=float(normalized_data[0][14]),
        item16=float(normalized_data[0][15]),
        outcome=outcome
    )

    try:
        # Criando sessão com a base de dados
        session = Session()

        # Adicionando o novo paciente à sessão
        session.add(novo_paciente)

        # Efetuando o commit para persistir as mudanças no banco de dados
        session.commit()

        # Registrando o sucesso na adição do paciente
        logger.debug(f"Novo paciente adicionado: '{novo_paciente.item1}'")

        # Retornando a representação do paciente recém-adicionado
        return apresenta_paciente(novo_paciente), 200

    # Em caso de erro na adição
    except Exception as e:
        # Mensagem de erro
        error_msg = "Não foi possível salvar o novo paciente"
        # Log do erro
        logger.warning(f"Erro ao adicionar novo paciente '{novo_paciente.item1}', {error_msg}")
        # Retornando mensagem de erro ao cliente
        return {"message": error_msg}, 400


# Rota para excluir um paciente pelo ID
@app.delete('/paciente_id', tags=[paciente_tag],
            responses={"200": PacienteDelIdSchema, "404": ErrorSchema})
def del_paciente_id(query: PacienteIdSchema):
    """Deleta um paciente a partir do id do paciente informado.
    """
    paciente_id = query.id
    print(paciente_id)
    logger.debug(f"Deletando dados sobre paciente #{paciente_id}")

    session = Session()

    count = session.query(Paciente).filter(Paciente.id== paciente_id).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado paciente #{paciente_id}")
        return {"mensagem": "Paciente removido", "id": paciente_id}
    else:
        error_msg = "Paciente não encontrado."
        logger.warning(f"Erro ao deletar paciente #'{paciente_id}', {error_msg}")
        return {"mensagem": error_msg}, 404    

# Rota de busca de paciente por ID
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteBuscaSchema, "404": ErrorSchema})
def get_paciente_id(query: PacienteIDBuscaSchema):    
    """Faz a busca por um paciente cadastrado na base a partir do ID.
    """
    
    paciente_id = query.id  # Ajuste aqui, obtendo o ID do objeto de consulta
    logger.debug(f"Coletando dados sobre paciente #{paciente_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(Paciente.id == paciente_id).first()
    
    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente com ID {paciente_id} não encontrado na base :/"
        logger.warning(f"Erro ao buscar paciente com ID '{paciente_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Paciente encontrado: '{paciente.id}'")
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200
