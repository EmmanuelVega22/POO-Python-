# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Bebida:
    
    __denominacion: str
    __presentacion: str
    __precio: float
    
    def __init__(self, denominacion, presentacion, precio):
        
        self.__denomiancion=denominacion
        self.__presentacion=presentacion
        self.__precio=precio
    
    def getPrecio(self):
        
        return self.__precio

    def getDenominacion(self):
        
        return self.__denomiancion