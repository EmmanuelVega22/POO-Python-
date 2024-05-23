# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseMatricula import Matricula

class GestorMatriculas:
    
    __listMatriculas: list
    
    def __init__(self):
        
        self.__listMatriculas = []
        
    def agregarMatriculas(self,nuevaMatricula):
        
        self.__listMatriculas.append(nuevaMatricula)
        
    
    def matricular_Empleados_EnProgramas(self,empleado,programa):
        
        fecha = input("Ingrese Fecha de Matriculacion: ")
        nuevaMatricula = Matricula(fecha,empleado,programa)
        
        self.agregarMatriculas(nuevaMatricula)
        
        return nuevaMatricula
    
    def mostrar(self):
        
        for i in range(len(self.__listMatriculas)):
            
            print(self.__listMatriculas[i])
            
    
    def buscarEmpleado(self,id_empleado):
        
       for i in range(len(self.__listMatriculas)):
           
           self.__listMatriculas[i].matriculasDeUnEmpleado(id_empleado)
    
    def buscarCapacitacion(self,nom_capacitacion):
        
        for i in range(len(self.__listMatriculas)):
            
            self.__listMatriculas[i].empleadosDeUnaCapacitacion(nom_capacitacion)
        
    
    