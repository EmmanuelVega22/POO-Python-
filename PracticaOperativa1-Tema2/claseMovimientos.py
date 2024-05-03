# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Movimientos:
    
    __nro_cuenta : int
    __fecha : str
    __descripcion : str
    __tipo_movimiento:str
    __importe : float
    
    
    def __init__(self,nro_cuenta,fecha,descripcion,tipo_movimiento,importe):
        
        self.__nro_cuenta = nro_cuenta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipo_movimiento = tipo_movimiento
        self.__importe = importe
    
    def __str__(self):
        
        return "%s %s %s %s %s" % (self.__nro_cuenta,self.__fecha,self.__descripcion,self.__tipo_movimiento,self.__importe)
    
    def getNroCuenta(self):
        
        return self.__nro_cuenta
    
    def getFecha(self):
        
        return self.__fecha
    
    def getDescripcion(self):
        
        return self.__descripcion
    
    def getTipoMovimiento(self):
        
        return self.__tipo_movimiento
    
    def getImporte(self):
        
        return self.__importe