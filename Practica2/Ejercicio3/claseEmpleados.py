# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Empleados:
    
    __nombre_apellido: str
    __id_empleado: int
    __puesto: str
    __matriculas: list
    
    def __init__(self,nomYapell,id_empleado,puesto):
        
        self.__nombre_apellido = nomYapell
        self.__id_empleado = id_empleado
        self.__puesto = puesto
        
        self.__matriculas = []
    
    def __str__(self):
        return f"Empleado: {self.__nombre_apellido}(ID: {self.__id_empleado}), Puesto: {self.__puesto}"
    
    def registrarMatriculas(self,nuevaMatricula):
        
        self.__matriculas.append(nuevaMatricula)
        
    def getNombreyApellido(self):
        
        return self.__nombre_apellido
    
    def getIdEmpleado(self):
        
        return self.__id_empleado
    
    def getPuesto(self):
        
        return self.__puesto
    
    def getListMatriculas(self):
        
        return self.__matriculas