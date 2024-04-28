# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Moto:
    
    __patente: str
    __marca: str
    __nombreC: str
    __apellidoC: str
    __kilometraje: int
    
    
    def __init__(self,patente,marca,nombreC,apellidoC,kilometraje):
        
        self.__patente = patente
        self.__marca = marca
        self.__nombreC = nombreC
        self.__apellidoC = apellidoC
        self.__kilometraje = kilometraje
    
    def __str__(self):
        
        return "%s %s %s %s %s" % (self.__patente, self.__marca, self.__nombreC, self.__apellidoC, self.__kilometraje)
   
    def getpatente(self):
        
        return self.__patente
    
    def getnombreC(self):
        
        return self.__nombreC
    
    def getapellidoC(self):
        
        return self.__apellidoC
    
        