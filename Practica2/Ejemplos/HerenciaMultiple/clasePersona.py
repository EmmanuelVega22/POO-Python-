# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:47:49 2024

@author: Emmanuel
"""

class Persona(object):
    
    __dni: int
    __apellido: str
    __nombre: str
    
    def __init__(self, dni, apellido, nombre, codigoCargo=0, agrupamiento=0,
                 catedra='', sueldo=0.0, fechaIngreso='', promedio=0.0, carrera=''):
        
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        
    def mostrarDatos(self):
        print(' _____________')
        print('|             |')
        print('|Datos Persona|')
        print('|_____________|')
        print('DNI: {0:9d}'.format(self.__dni))
        print('Apellido: {}, Nombre: {}'.format(self.__apellido, self.__nombre))