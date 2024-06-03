# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Nodo:
    
    __calefactores = object
    __siguiente = object
    
    def __init__(self,calefactores):
        
        self.__calefactores = calefactores
        
        self.__siguiente = None
        
    
    def getSiguiente(self):
        
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        
        self.__siguiente = siguiente
    
    def getDato(self):
        
        return self.__calefactores
        
    