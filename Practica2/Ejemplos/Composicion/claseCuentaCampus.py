# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class CuentaCampus:
    #Variables de clase
    __dominio='@unsj-cuim.edu.ar'
    __idCuenta=0
    # Variables de instancia
    __idUsuario: int
    __nombreUsuario: str
    __clave: str
    
    # Métodos de clase
    @classmethod
    def getDominio(cls):
        
        return cls.__dominio
    
    @classmethod
    def getIdCuenta(cls):

        cls.__idCuenta+=1
        return cls.__idCuenta
    
    # Métodos de instancia
    def __init__(self, idUsuario, nombreUsuario, clave):
        
        self.__idUsuario=idUsuario
        self.__nombreUsuario=nombreUsuario
        self.__clave=clave
        
    def __str__(self):
        
        cadena = 'Usuario: {}\nClave {}'.format(self.__nombreUsuario,self.__clave)
        return cadena
    
    def cambiarClave(self, nuevaClave):
        
        self.__clave=nuevaClave


    def mostrar(self):

    	print(self)