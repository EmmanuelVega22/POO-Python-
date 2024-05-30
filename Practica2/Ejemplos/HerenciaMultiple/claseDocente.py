# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from clasePersona import Persona

class Docente(Persona):

    __codigoCargo: str
    __agrupamiento: int
    __catedra: str
    __sueldo: float

    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera,
                 codigoCargo, agrupamiento, catedra, sueldo):
        
        super().__init__(dni, apellido, nombre, fechaIngreso, promedio,
             carrera, codigoCargo, agrupamiento,catedra, sueldo)

        self.__codigoCargo=codigoCargo
        self.__agrupamiento=agrupamiento
        self.__catedra=catedra
        self.__sueldo=sueldo

    def mostrarDatos(self):

        super().mostrarDatos()
        print(' _____________')
        print('|             |')
        print('|Datos Docente|')
        print('|_____________|')
        print('Codigo cargo {}/{}'.format(self.__codigoCargo, self.__agrupamiento))
        print('Cátedra: {0}, sueldo ${1:8.2f}'.format(self.__catedra, self.__sueldo))