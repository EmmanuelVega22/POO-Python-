# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseProgramaCapacitacion import ProgramaCapacitacion

class GestorProgramaCapacitacion:
    
    __listProgramaCapacitacion: list
    
    
    def __init__(self):
        
        self.__listProgramaCapacitacion = []   
    
    def agregarProgramaCapacitacion(self,nuevoPrograma):
        
        self.__listProgramaCapacitacion.append(nuevoPrograma)
        
    def cargarProgramasCapacitacion(self):
        
        print(" _________________________________")
        print("|                                 |")
        print("|  Cargar Programas Capacitacion  |")
        print("|_________________________________|")
        
        op = 'si'
        
        while op.lower() == 'si':
            
            nombre = input("Ingrese Nombre: ")            
            while True:
               
                try:
                    
                    codigo = int(input("Ingrese Codigo Programa: "))
                    duracion = int(input("Ingrese Duracion Programa: "))

                    break
                
                except ValueError: #Operación sobre un objeto de tipo correcto pero valor inapropiado
                    
                    print("Por favor, ingrese un número válido para codigo y/o duracion.")
            
            nuevoPrograma = ProgramaCapacitacion(nombre,codigo,duracion)
            
            self.agregarProgramaCapacitacion(nuevoPrograma)
            
            op = input("Cargar Otra Capacitacion? ('Si' o 'No'):\n")
            
    
    
    def buscarProgramaCapacitacion(self,nom_programa):
        
        
        i = 0
        
        while i<len(self.__listProgramaCapacitacion) and self.__listProgramaCapacitacion[i].getNombre() != nom_programa:
            
            i+=1
        
        try:
        
            if self.__listProgramaCapacitacion[i].getNombre() == nom_programa:
            
                return self.__listProgramaCapacitacion[i]
        
        except IndexError:
            
            return None
    
    def registrarMatriculas(self,nuevaMatricula,i):
        
        
        self.__listProgramaCapacitacion[i].cargarMatricula(nuevaMatricula)

    
    def mostrar(self):
        
        
        for i in range(len(self.__listProgramaCapacitacion)):
            
            print(self.__listProgramaCapacitacion[i])
            
    def matriculasDeUnEmpleado(self,i):
        
            print("Matricula:\n")
            print("Programa de Capacitacion:{}\n".format(self.__listProgramaCapacitacion[i].getNombre()))
            print("Duracion: {}\n".format(self.__listProgramaCapacitacion[i].getDuracion()))
