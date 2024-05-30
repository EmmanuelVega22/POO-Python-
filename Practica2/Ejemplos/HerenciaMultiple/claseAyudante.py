# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseDocente import Docente
from claseAlumno import Alumno

class Ayudante(Docente, Alumno): #De Derecha a Izquierda Significa en que orden
                                #heredara los datos y en que orden los mostrara

    __concepto: str
    __horasLIA: int

    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera, codigoCargo, agrupamiento, catedra, sueldo, concepto, horasLIA=0):

        super().__init__(dni, apellido, nombre, fechaIngreso, promedio, carrera, codigoCargo, agrupamiento, catedra, sueldo)
        self.__concepto=concepto
        self.__horasLIA=horasLIA

    def mostrarDatos(self):

        super().mostrarDatos()
        print(' ______________')
        print('|              |')
        print('|Datos Ayudante|')
        print('|______________|')
        print('Horas LIA {}'.format(self.__horasLIA))
        print('Concepto: {}'.format(self.__concepto))