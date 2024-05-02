# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Cuenta:
    
    __nombre : str
    __apellido: str
    __dni : int
    __telefono : int
    __saldo : float
    __CVU : str
    porcentaje_anual = 68
    
    
    def __init__(self,nombre,apellido,dni,telefono,saldo,cvu):
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__telefono = telefono
        self.__saldo = saldo
        self.__CVU = cvu
        
     
    def __str__(self):
        
        return "%s %s %s %s %s %s" % (self.__nombre,self.__apellido, self.__dni, self.__telefono,self.__saldo,self.__CVU)
   
    def obtener_datos_como_lista(self):
        
        return [self.__nombre, self.__apellido, self.__dni,self.__telefono,self.__saldo,self.__CVU]
    
    
    def getNombre(self):
        
        return self.__nombre
    
    def getApellido(self):
        
        return self.__apellido
    
    def getDni(self):
        
        return self.__dni
    
    def getCVU(self):
        
        return self.__CVU
    
    def getSaldo(self):
        
        return float(self.__saldo)
    
    def setSaldo(self,nuevoSaldo):
        
        self.__saldo = nuevoSaldo
    
    @classmethod  
    def getPorcentajeAnual(cls):
        
        return float(cls.porcentaje_anual)
    
    @classmethod    
    def setPorcentajeAnual(cls,nuevoPorcentaje):
        
        cls.porcentaje_anual = nuevoPorcentaje