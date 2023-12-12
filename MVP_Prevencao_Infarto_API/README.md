# Prevencao de Infarto- MVP


O ataque cardíaco é uma condição séria que atinge indivíduos de todas as faixas etárias em todo o mundo, constituindo uma causa crucial de mortalidade global.

O efeito do infarto cardíaco na saúde pública é considerável, necessitando de ações preventivas para minimizar seu impacto. Incorporar hábitos saudáveis, como uma dieta balanceada, exercícios regulares e controle dos fatores de risco, é fundamental para evitar possíveis complicações.

A questão foi tratada como um procedimento de categorização, envolvendo etapas de modelagem, inferência, formulação e avaliação de modelos.

Os dados foram submetidos a processos de normalização e ajuste de hiperparâmetros, destacando-se que o Naive Bayes apresentou a melhor acurácia. Subsequentemente, foi gerado um arquivo pkl contendo o modelo treinado, o qual foi integrado ao backend do sistema para servir como um modelo capacitado para previsões.

Ao disponibilizar informações personalizadas, busca-se conscientizar sobre a relevância da análise de riscos individuais e incentivar a adoção de um modo de vida saudável. O propósito do projeto é contribuir para o desenvolvimento de uma sociedade mais saudável e resistente diante das condições cardiovasculares.

O projeto visa contribuir para uma sociedade mais saudável.


O dataset utilizado para o projeto pode ser encontrado [aqui](https://github.com/gabrigon0706/Prevencao_Infarto_Database).

O notebook no Google Colab pode ser encontrado [aqui](https://colab.research.google.com/drive/15usZWOn5Vfu4lidAp7IPTO1PTUuEkVN2).

O vídeo sobre projeto pode ser encontrado [aqui](https://www.youtube.com/watch?v=f1EnrIXY-TI).

O back-end pode ser encontrado [aqui](https://github.com/gabrigon0706/MVP_Prevencao_Infarto_Main/tree/main/MVP_Prevencao_Infarto_API).

O front-end pode ser encontrado [aqui](https://github.com/gabrigon0706/MVP_Prevencao_Infarto_Main/tree/main/MVP_Prevencao_Infarto_Front).


## Requisitos

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal.

Certifique-se de que você tenha  todas as libs python listadas no `requirements.txt` instaladas.

Este comando instala as bibliotecas, descritas no arquivo `requirements.txt`:

pip install -r requirements.txt

## Como Usar

Para utilizar esta API, siga os passos abaixo:

1. Inicie a aplicação Flask:

  flask run --host 0.0.0.0 --port 5000

2. Acesse a documentação Swagger para obter detalhes sobre as rotas e os parâmetros necessários.

3. Use as rotas para adicionar, visualizar ou remover dados de pacientes.

## Documentação Swagger

Para obter a documentação completa desta API no estilo Swagger, acesse: 
[http://localhost:5000//openapi/swagger#/](http://localhost:5000//openapi/swagger#/)

## Rotas da API

- [GET] `/paciente`

  Faz a busca por um paciente cadastrado na base a partir do ID.

- [POST] `/paciente`

  Faz a adição de um novo paciente na base de dados.

  - **Entrada**: Um objeto JSON com os dados do paciente.
  - **Saída**: Uma representação dos dados do paciente cadastrados.

- [DELETE] `/paciente_id`

  Deleta um paciente a partir do ID do paciente informado.

- [GET] `/pacientes`

  Lista todos os pacientes cadastrados na base.

## Teste Automatizado
- Para executar o pytest utilize o seguinte comando:

  pytest -v test_modelos.py

## Funcionalidade disponivel

- Funcionalidade de inserir dados através de um questionário.
- Gerar uma predição.
   
## Autor

Este projeto foi desenvolvido por Gabriel Gonçalves e pode ser encontrado no [GitHub](https://github.com/gabrigon0706).
