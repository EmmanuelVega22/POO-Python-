# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:51:19 2024

@author: Emmanuel
"""

class Plato:
    
    __descripcion: str
    __precio: float

    def __init__(self, descripcion, precio):
        
        self.__descripcion=descripcion
        self.__precio=precio
        
    def getPrecio(self):

        return self.__precio
    
    def getDescripcion(self):
        
        return self.__descripcion