# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseNodo import Nodo
from claseProfesor import Profesor

class Lista:
    
    __cabeza: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        
        self.__cabeza = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
        
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        if self.__indice == self.__tope:
            
            self.__actual = self.__cabeza
            self.__indice = 0
            raise StopIteration
        
        else:
            
            self.__indice +=1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
        
    def cargarProfesores(self):
        
        
        op = 'si'
        
        while op !='NO':
            
            if self.__cabeza == None:
                
                dni = int(input("Ingrese DNI: "))
                nombre = input("Ingrese Nombre: ")
                apellido = input("Ingrese Apellido: ")
                puesto = input("Ingrese Puesto: ")
                
                profesor = Profesor(dni,nombre,apellido,puesto)
                
                nodo = Nodo(profesor)
                self.__cabeza = nodo
                self.__actual = nodo
                self.__tope +=1
            
            else:
                
                aux = self.__cabeza
                
                while aux.getSiguiente() != None:
                    
                    aux = aux.getSiguiente()
                    
                    
                dni = int(input("Ingrese DNI: "))
                nombre = input("Ingrese Nombre: ")
                apellido = input("Ingrese Apellido: ")
                puesto = input("Ingrese Puesto: ")
                
                profesor = Profesor(dni,nombre,apellido,puesto)
                
                nodo = Nodo(profesor)
                aux.setSiguiente(nodo)
                self.__tope +=1
                self.__actual = self.__cabeza
        
            op = input("¿Cargar otro Profesor? (Si/No): ").upper()
        
        
             
    def eliminarProfesorPorDni(self, dni):
        
        aux=self.__cabeza
        encontrado = False
        
        if aux.getDato().getDNI()==dni:
            
            encontrado=True
            print('Encontrado y eliminado:\n'+str(aux.getDato()))
            self.__cabeza = aux.getSiguiente() #Caso que este en la cabeza
            self.__tope-=1
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
            
            while not encontrado and aux != None:
                if aux.getDato().getDNI()==dni: #Caso que este en la cola
                    encontrado=True
                else:
                    ant = aux
                    aux=aux.getSiguiente()
            if encontrado:
                print('Encontrado y eliminado:\n'+str(aux.getDato()))
                ant.setSiguiente(aux.getSiguiente())
                self.__tope-=1
                del aux
            else:
                print('El DNI {}, no está en la lista'.format(dni))
                
    
    