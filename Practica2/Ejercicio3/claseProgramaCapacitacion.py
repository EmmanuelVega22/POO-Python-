# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class ProgramaCapacitacion:
    
    __nombre: str
    __codigo: int
    __duracion: int
    __matriculas:list 
    
    def __init__(self,nombre,codigo,duracion):
        
        self.__nombre = nombre
        self.__codigo = codigo
        self.__duracion = duracion 
        self.__matriculas = []
     
    def __str__(self):
        return f"Programa de Capacitación: {self.__nombre}, Código: {self.__codigo}, Duración: {self.__duracion} horas"
    
    def cargarMatricula(self,nuevaMatricula):
        
        self.__matriculas.append(nuevaMatricula)
        
    def getNombre(self):
        
        return self.__nombre
    
    def getCodigo(self):
        
        return self.__codigo
    
    def getDuracion(self):
        
        return self.__duracion
        
        