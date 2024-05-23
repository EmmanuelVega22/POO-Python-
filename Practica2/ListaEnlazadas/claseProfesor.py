# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseCuentaCampus import CuentaCampus
class Profesor:
    
    __dni:int
    __nombre:str
    __apellido:str
    __puesto:str
    __cuentaCampus: object
    
    def __init__(self,dni,nombre,apellido,puesto):
        
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__puesto = puesto
        id_cuenta = CuentaCampus.getIdCuenta()
        dominio = CuentaCampus.getDominio()
        usuario = nombre.lower()+apellido.lower()+dominio
        self.__cuentaCampus = CuentaCampus(id_cuenta,usuario,dni)
    
    
    def __del__(self):
        
        print('Borrando cuenta de usuario....')
        del self.__cuentaCampus
    
    def __str__(self):
        
        cadena ='Profesor: \n'
        cadena += 'Apellido y nombre: {}, {}\n'.format(self.__apellido, self.__nombre)
        cadena+=str(self.__cuentaCampus)
        return cadena
    
    def getDNI(self):
        
        return self.__dni
    
    def getNombre(self):
        
        return self.__nombre
    
    def getApellido(self):
        
        return self.__apellido
    
    def getPuesto(self):
        
        return self.__puesto