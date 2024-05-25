# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:31:49 2024

@author: Emmanuel
"""

class Nodo:
    
    __inmuebles = object
    __siguiente = object
    
    def __init__(self,inmueble):
        
        self.__inmuebles = inmueble
        
        self.__siguiente = None
        
    def __str__(self):
        
        return str(self.__inmuebles)
    
    def getSiguiente(self):
        
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        
        self.__siguiente = siguiente
           
    def getDato(self):
        
        return self.__inmuebles
        
        