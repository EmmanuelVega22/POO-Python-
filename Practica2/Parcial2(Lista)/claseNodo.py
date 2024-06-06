# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 03:02:40 2024

@author: USUARIO
"""

class Nodo:
    
    __productos:object
    __siguiente: object
    
    def __init__(self,producto):
        
        self.__productos = producto
        self.__siguiente = None
        
    
    def getSiguiente(self):
        
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        
        self.__siguiente = siguiente
    
    
    def getDato(self):
        
        return self.__productos