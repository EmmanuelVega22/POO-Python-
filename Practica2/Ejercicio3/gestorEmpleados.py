# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseEmpleados import Empleados

class ProgramaNoEncontradoError(Exception): #Excepcion Personalizadas
        #Se define como clase
        pass

class GestorEmpleados:
    
    __listEmpleados: list
    
    
    def __init__(self):
        
        self.__listEmpleados = []  
    
    def agregarEmpleados(self,nuevoEmpleado):
        
        self.__listEmpleados.append(nuevoEmpleado)
    
    
    
    def cargarEmpleados(self,gprograma):
        
        print(" ____________________")
        print("|                    |")
        print("|  Cargar Empleados  |")
        print("|____________________|")
        
        op = 'si'
        
        while op.lower() == 'si':
            
            nya = input("Ingrese Nombre y Apellido: ")
            puesto = input("Ingrese Puesto: ")
            
            while True:
               
                try:
                    
                    id_empleado = int(input("Ingrese ID Empleado: "))
                    break
                
                except ValueError: #Operación sobre un objeto de tipo correcto pero valor inapropiado
                    
                    print("Por favor, ingrese un número válido para ID Empleado.")
            
            nuevoEmpleado = Empleados(nya,id_empleado,puesto)
            
            self.agregarEmpleados(nuevoEmpleado)
            
            op = input("Cargar Otro Empleado? ('Si' o 'No'):\n")
            
            
    def registrarEmpleado_Programa(self,programa,matricula):
        
        posicion = 0
        for i in range(len(self.__listEmpleados)):
            
            nom_programa = input("Ingrese Nombre del Programa de Capacitacion del empleado '{}': ".format(self.__listEmpleados[i].getNombreyApellido()))
            
            while nom_programa.lower() != 'fin':
            
                capacitacion = programa.buscarProgramaCapacitacion(nom_programa)
                    
                if capacitacion != None:
                
                    op = input("El Empleado {} ha sido matriculacion en el programa {}? ('Si' o 'No'):\n".format(self.__listEmpleados[i].getNombreyApellido(),nom_programa))
                
                    if op.lower() == 'si':
                        nuevaMatricula = matricula.matricular_Empleados_EnProgramas(self.__listEmpleados[i], capacitacion)
                        self.__listEmpleados[i].registrarMatriculas(nuevaMatricula)
                        programa.registrarMatriculas(nuevaMatricula, posicion)
                        posicion += 1
                #except ProgramaNoEncontradoError:
                    
                    #print("El programa de capacitación '{}' no se encontró.".format(nom_programa))
                else:
                    
                    print("El programa de capacitación '{}' no se encontró.".format(nom_programa))

                nom_programa = input("Ingrese Nombre de otro Programa de Capacitacion del Empleado '{}' ('FIN' para terminar): ".format(self.__listEmpleados[i].getNombreyApellido()))

    def mostrar(self):
        
        for i in range(len(self.__listEmpleados)):
            
            print(self.__listEmpleados[i])         
    
    
    def buscarEmpleadosConMatriculacion(self):
        
        for i in range(len(self.__listEmpleados)):
            
            if len(self.__listEmpleados[i].getListMatriculas()) == 0:
                
                print("El Empleado {} no poseea ninguna matriculacion de ningun programa de capacitacion".format(self.__listEmpleados[i].getNombreyApellido()))
            
            #self.__listEmpleados[i].matriculacionDelEmpleado()