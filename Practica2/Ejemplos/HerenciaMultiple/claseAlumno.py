# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from clasePersona import Persona

class Alumno(Persona):

    __fechaIngreso: str
    __promedio: float
    __carrera: str
    
    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera,
                 codigoCargo, agrupamiento,catedra, sueldo):
        
        super().__init__(dni, apellido, nombre, fechaIngreso, promedio,
             carrera, codigoCargo, agrupamiento,catedra, sueldo)
        
        self.__fechaIngreso=fechaIngreso
        self.__promedio=promedio
        self.__carrera=carrera

    def mostrarDatos(self):

        super().mostrarDatos()
        print(' ____________')
        print('|            |')
        print('|Datos Alumno|')
        print('|____________|')
        print('Carrera: {}, fecha de ingreso: {}'.format(self.__carrera, self.__fechaIngreso))
        print('Promedio {0}'.format(self.__promedio))