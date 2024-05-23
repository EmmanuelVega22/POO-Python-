# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class CuentaCampus:
    
    __dominio = 'unsj-cuim.edu.ar'
    __idCuenta = 0
    __id_usuario = int
    __nombreUsuario = str
    __clave: str
    
    
     # Métodos de clase
    @classmethod
    def getDominio(cls):
        
        return cls.__dominio
    
    @classmethod
    def getIdCuenta(cls):

        cls.__idCuenta+=1
        return cls.__idCuenta
    
    def __init__(self,usuario,nombre_usuario,clave):
        
        self.__id_usuario = usuario
        self.__nombreUsuario = nombre_usuario
        self.__clave = clave
        
    def __str__(self):
        
        cadena = 'Usuario: {}\nClave {}'.format(self.__nombreUsuario,self.__clave)
        return cadena
    
    def cambiarClave(self, nuevaClave):
        
        self.__clave=nuevaClave