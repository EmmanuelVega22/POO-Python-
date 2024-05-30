# -*- coding: utf-8 -*-
"""

@author: Emmanuel
"""

class Nodo:
    
    __profesor: object
    __siguiente: object
    
    def __init__(self,profesor):
        
        self.__profesor = profesor
        self.__siguiente = None
        
    def getSiguiente(self):
        
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        
        self.__siguiente = siguiente
        
    def getDato(self):
        
        return self.__profesor