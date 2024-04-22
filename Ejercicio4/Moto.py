# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Moto:
    
    __patente : str
    __marca : str
    __nombreC : str
    __apellidoC: str
    __kilometraje: int

    def __init__(self,patente,marca,nombreC,apellidoC,kilometraje):

        self.__patente = patente
        self.__marca = marca
        self.__nombreC = nombreC
        self.__apellidoC = apellidoC
        self.__kilometraje = kilometraje


    def agregarMotos(self,nuevaMoto):

        self.__listMotos.append(nuevaMoto)