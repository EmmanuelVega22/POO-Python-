# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Gobernador:
    
    __dni: int
    __nombreApellido: str
    __provincia: object
    
    def __init__(self, dni, nombreApellido, provincia=None):
        self.__dni=dni
        self.__nombreApellido=nombreApellido
        self.__provincia=provincia
    
    def __str__(self):
        cadena = 'DNI: %d, Nombre y Apellido: %s' % (self.__dni,
        self.__nombreApellido)
        return cadena
    
    def setProvincia(self, provincia):
        self.__provincia=provincia