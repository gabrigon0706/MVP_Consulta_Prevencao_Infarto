# Prevencao de Infarto- MVP

O ataque cardíaco é uma condição séria que atinge indivíduos de todas as faixas etárias em todo o mundo, constituindo uma causa crucial de mortalidade global.

O efeito do infarto cardíaco na saúde pública é considerável, necessitando de ações preventivas para minimizar seu impacto. Incorporar hábitos saudáveis, como uma dieta balanceada, exercícios regulares e controle dos fatores de risco, é fundamental para evitar possíveis complicações.

Este projeto passou por um processo de criação de um modelo de machine learning em um notebook no Google Colab, que pode ser encontrado [neste link](https://colab.research.google.com/drive/15usZWOn5Vfu4lidAp7IPTO1PTUuEkVN2).


A questão foi tratada como um procedimento de categorização, envolvendo etapas de modelagem, inferência, formulação e avaliação de modelos.

Os dados foram submetidos a processos de normalização e ajuste de hiperparâmetros, destacando-se que o Naive Bayes apresentou a melhor acurácia. Subsequentemente, foi gerado um arquivo pkl contendo o modelo treinado, o qual foi integrado ao backend do sistema para servir como um modelo capacitado para previsões.

Ao disponibilizar informações personalizadas, busca-se conscientizar sobre a relevância da análise de riscos individuais e incentivar a adoção de um modo de vida saudável. O propósito do projeto é contribuir para o desenvolvimento de uma sociedade mais saudável e resistente diante das condições cardiovasculares.


## Descrição

O sistema permite que os usuários respondam um questionário que visa obter dados sobre: Idade, Sexo, Colesterol, Batimento cardíaco, Diabetes, Histórico na família, Fumante, Obesidade,Consumo de álcool, Dieta, Problema cardíaco, Uso de medicação, Nível de estresse, Triglicerídeos, Atividade física na semana, Horas de sono.

Com esses dados é possível realizar uma predição de risco de infarto cardíaco, utilizando o modelo de machine learning Naive Bayes (NB). 

O DataSet utilizado para o projeto pode ser encontrado [aqui](https://github.com/gabrigon0706/Prevencao_Infarto_Database).

O notebook no Google Colab pode ser encontrado [aqui](https://colab.research.google.com/drive/15usZWOn5Vfu4lidAp7IPTO1PTUuEkVN2).

O vídeo sobre projeto pode ser encontrado [aqui](https://www.youtube.com/watch?v=f1EnrIXY-TI).

O back-end pode ser encontrado [aqui](https://github.com/gabrigon0706/MVP_Prevencao_Infarto_Main/tree/main/MVP_Prevencao_Infarto_API).

O front-end pode ser encontrado [aqui](https://github.com/gabrigon0706/MVP_Prevencao_Infarto_Main/tree/main/MVP_Prevencao_Infarto_Front).

## Funcionalidade disponivel

- Funcionalidade de inserir dados através do formulario.
- Gerar um resultado a partir dos dados fornecidos.
   
## Autor

Este projeto foi desenvolvido por Gabriel Gonçalves e pode ser encontrado no [GitHub](https://github.com/gabrigon0706).

