
from datetime import date, datetime


class Poluicao:
    def __init__(self, id, data:datetime, ozonio, material_particulado, monox_carbono, ox_Nitroso, gas, temperatura, umidade ):
        self.__data = data
        self.__id = id
        self.__ozonio = ozonio
        self.__material_particulado = material_particulado
        self.__monox_carbono = monox_carbono
        self.__ox_Nitroso = ox_Nitroso
        self.__gas = gas
        self.__temperatura = temperatura
        self.__umidade = umidade
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,valor):
        self.__id = valor
        
    @property
    def data(self)-> datetime:
        return self.__data
    @data.setter
    def data(self,valor:datetime):
        self.__data = valor
    
    @property
    def ozonio(self):
        return self.__ozonio
    @ozonio.setter
    def ozonio(self,valor):
        self.__ozonio = valor
    
    @property
    def material_particulado(self):
        return self.__material_particulado
    @material_particulado.setter
    def material_particulado(self,valor):
        self.__material_particulado = valor
    
    @property
    def monox_carbono(self):
        return self.__monox_carbono
    @monox_carbono.setter
    def monox_carbono(self,valor):
        self.__monox_carbono = valor
    
    @property
    def ox_Nitroso(self):
        return self.__ox_Nitroso
    @ox_Nitroso.setter
    def ox_Nitroso(self,valor):
        self.__ox_Nitroso = valor
    
    @property
    def gas(self):
        return self.__gas
    @gas.setter
    def gas(self,valor):
        self.__gas = valor
    
    @property
    def temperatura(self):
        return self.__temperatura
    @temperatura.setter
    def temperatura(self,valor):
        self.__temperatura = valor
    
    @property
    def umidade(self):
        return self.__umidade
    @umidade.setter
    def umidade(self,valor):
        self.__umidade = valor
    
    def toJson(self):
        return {
            "Detector": self.__id,
            "data": self.__data.strftime('%d/%m/%Y %H:%M'),
            "Ozonio": self.__ozonio,
            "Material Particulado": self.__material_particulado,
            "Monoxido de Carbono": self.__monox_carbono,
            "Oxido Nitroso": self.__ox_Nitroso,
            "Gas": self.__gas,
            "Temperatura": self.__temperatura,
            "Umidade": self.__umidade
        }
    