# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Paciente:
    
    __dni: int
    __apellido: str
    __nombre: str
    __prescripciones: list
    
    def __init__(self, dni, apellido, nombre):
        
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__prescripciones = []
        
    def addPrescripcion(self, prescripcion):
        
        self.__prescripciones.append(prescripcion)