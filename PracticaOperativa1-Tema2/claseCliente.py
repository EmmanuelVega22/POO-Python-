# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Clientes:
    
    __nombre:str
    __apellido:str
    __dni : int
    __nro_cuenta: int
    __saldo:float
    
    
    def __init__(self,nombre,apellido,dni,nro_cuenta,saldo_anterior):
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__nro_cuenta = nro_cuenta
        self.__saldo = saldo_anterior
        
    def __str__(self):
        
        return "%s %s %s %s %s" % (self.__nombre,self.__apellido,self.__dni,self.__nro_cuenta,self.__saldo)
    def getNombre(self):
        
        return self.__nombre
    
    def getApellido(self):
        
        return self.__apellido
    
    def getDni(self):
        
        return self.__dni
    
    def getNroCuenta(self):
        
        return self.__nro_cuenta
    
    def getSaldo(self):
        
        return self.__saldo
        
    def setSaldo(self,nuevoSaldo):
        
        self.__saldo = nuevoSaldo