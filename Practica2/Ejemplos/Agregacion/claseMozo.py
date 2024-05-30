# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:52:20 2024

@author: Emmanuel
"""

class Mozo:
    
    __idMozo: int
    __apellido: str
    __nombre: str

    def __init__(self, idMozo, apellido, nombre):

        self.__idMozo=idMozo
        self.__apellido=apellido
        self.__nombre=nombre