
class Poluicao:
    def __init__(self, ozonio, material_particulado, monox_carbono, ox_Nitroso, gas, temperatura, umidade ):
        self.__ozonio = ozonio
        self.__material_particulado = material_particulado
        self.__monox_carbono = monox_carbono
        self.__ox_Nitroso = ox_Nitroso
        self.__gas = gas
        self.__temperatura = temperatura
        self.__umidade = umidade
    
    @property
    def ozonio(self):
        return self.__ozonio
    
    @property
    def material_particulado(self):
        return self.__material_particulado
    
    @property
    def monox_carbono(self):
        return self.__monox_carbono
    
    @property
    def ox_Nitroso(self):
        return self.__ox_Nitroso
    
    @property
    def gas(self):
        return self.__gas
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @property
    def umidade(self):
        return self.__umidade
    
    def toJson(self):
        return {
            'Ozonio': self.__ozonio,
            'Material Particulado': self.__material_particulado,
            'Monoxido de Carbono': self.__monox_carbono,
            'Oxido Nitroso': self.__ox_Nitroso,
            'Gas': self.__gas,
            'Temperatura': self.__temperatura,
            'Umidade': self.__umidade
        }
    