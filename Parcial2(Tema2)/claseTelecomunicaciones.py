
import abc
from abc import ABC

class Telecomunicaciones(ABC):

    __nom_compania:str
    __duracion_plan:str
    __cobertura_geografrica:str
    __precio_base:float

    def __init__(self,nombre,duracion,cobertura,precio):

        self.__nom_compania = nombre
        self.__duracion_plan = duracion
        self.__cobertura_geografrica = cobertura
        self.__precio_base = precio

    def __str__(self):

        cadena = 'Telecomunicaciones:\n'
        cadena += "Nombre Compania: " + self.__nom_compania + '\n'
        cadena += "Duracion Plan: " + self.__duracion_plan + '\n'
        cadena += "Cobertura Geografica: " + self.__cobertura_geografrica + '\n'
        cadena += "Precio Base: " + self.__precio_base + '\n'

        return cadena
    def getNombreCompania(self):

        return self.__nom_compania
    
    def getDuracionPlan(self):

        return self.__duracion_plan
    
    def getCoberturaGeografica(self):

        return self.__cobertura_geografrica
    
    def getPrecioBase(self):

        return self.__precio_base
    
    @abc.abstractmethod
    def importeDePlan(self):

        pass
