from datetime import datetime
from application.model.entity.detector import Poluicao
class Detector_dao:
    def __init__(self):
        self.__resultados = [Poluicao("escola", datetime.now(), 44, 76, 56, 42, 14, 64, 22),
            Poluicao("prefeitura-vassouras", datetime.now() , 44, 76, 56, 42, 14, 64, 22)]
        
    def resultados_list(self):
        return self.__resultados