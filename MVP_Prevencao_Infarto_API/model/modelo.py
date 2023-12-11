import logging
import joblib
import numpy as np


class Model:
    logger = logging.getLogger(__name__)

    @staticmethod
    def carrega_modelo(path_modelo, path_scaler):
        """Carrega um modelo a partir de um arquivo .pkl e um scaler
        """
        try:
            if path_modelo.endswith('.pkl') and path_scaler.endswith('.pkl'):
                model = joblib.load(path_modelo)
                scaler = joblib.load(path_scaler)
                Model.logger.info(f"Modelo e scaler carregados com sucesso.")
            else:
                raise Exception('Formato de arquivo não suportado. Apenas arquivos .pkl são suportados.')
            
            return model, scaler
        except Exception as e:
            Model.logger.error(f"Erro ao carregar modelo e scaler: {str(e)}")
            raise Exception(f"Erro ao carregar modelo e scaler: {str(e)}")

    @staticmethod
    def preditor(model, scaler, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        # Aplicando a normalização do scaler aos dados de entrada
        X_input = scaler.transform(np.array([
                        form[0], form[1], form[2], form[3], 
                        form[4], form[5], form[6], form[7],
                        form[8], form[9], form[10], form[11],
                        form[12], form[13], form[14], form[15]
                    ]).reshape(1, -1))

        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input)
        return int(diagnosis[0])