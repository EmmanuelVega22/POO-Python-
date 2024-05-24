
from clasePublicaciones import Publicaciones

class Nodo:

    __publicaciones: Publicaciones

    __siguiente: object

    def __init__(self, publicaciones):
        
        self.__publicaciones = publicaciones
        self.__siguiente = None


    def __str__(self):

        return str(self.__publicaciones)
    
    def getSiguiente(self):

        return self.__siguiente
    
    def setSiguiente(self,siguiente):

        self.__siguiente = siguiente

    def getDato(self):

        return self.__publicaciones

