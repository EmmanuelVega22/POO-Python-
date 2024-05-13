# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Matricula:
    
    __fecha:str
    __empleados: object
    __programas: object
    
    def __init__(self,fecha,empleados,programa):
        
        self.__fecha = fecha
        self.__empleados = empleados
        self.__programas = programa
        
    def __str__(self):
        
        cadena = 'Fecha'+self.__fecha+'\n'
        cadena +=str(self.__empleados)+'\n'
        cadena +=str(self.__programas)+'\n'
        return cadena
    
    def matriculasDeUnEmpleado(self,id_empleado):
        
        if self.__empleados.getIdEmpleado() == id_empleado:
            
            print("Empleado: {}\t\tID:{}".format(self.__empleados.getNombreyApellido(),self.__empleados.getIdEmpleado()))
            print("Matriculas:")
            print("Programa Capacitacion: {}\t\tDuracion:{}\n".format(self.__programas.getNombre(),self.__programas.getDuracion()))
    
    def empleadosDeUnaCapacitacion(self,nom_capacitacion):
        
        if self.__programas.getNombre() == nom_capacitacion:
            
            print(self.__empleados)