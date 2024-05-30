# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Provincia:
    
    __nombre: str
    __cantidadDeHabitantes: int
    __gobernador: object
    
    def __init__(self, nombre, cantidadDeHabitantes,
        gobernador=None):
        self.__nombre=nombre
        self.__cantidadDeHabitantes=cantidadDeHabitantes
        self.__gobernador=gobernador
    
    def __str__(self):
        return 'Provincia: %s, habitantes %d, gobernada por: %s' % (self.__nombre, self.__cantidadDeHabitantes, self.__gobernador)
    
    def setGobernador(self, gobernador):
        self.__gobernador=gobernador