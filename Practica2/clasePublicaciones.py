
import abc

from abc import ABC

class Publicaciones(ABC):

    __titulo: str
    __categoria: str
    __precio_base: float


    def __init__(self,titulo,categoria,precio_base):

        self.__titulo = titulo
        self.__categoria = categoria
        self.__precio_base = precio_base

    def getTitutlo(self):

        return self.__titulo
    
    def getCategoria(self):

        return self.__categoria
    
    def getPrecioBase(self):

        return self.__precio_base
    
    @abc.abstractmethod
    def importeVenta(self):

        pass    