# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:37:56 2024

@author: Emmanuel
"""

class Transacciones:
    
    __CVU: str
    __num_transaccion: int
    __importe: float
    __tipo_transaccion: str #D: debito C:credito
    
    def __init__(self,cvu,num_transaccion,importe,tipo_transaccion):
        
        self.__CVU = cvu
        self.__num_transaccion = num_transaccion
        self.__importe = importe
        self.__tipo_transaccion = tipo_transaccion
    
    def __str__(self):
        
        return "%s %s %s %s" % (self.__CVU,self.__num_transaccion, self.__importe, self.__tipo_transaccion)
   
    
    def getCVU(self):
        
        return self.__CVU
    
    def getTipo_transaccion(self):
        
        return self.__tipo_transaccion
    
    def getImporte(self):
        
        return float(self.__importe)