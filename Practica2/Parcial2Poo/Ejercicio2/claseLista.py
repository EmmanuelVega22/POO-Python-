# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseNodo import Nodo
from claseCasa import Casa
from claseDepartamento import Departamento

class Lista:
    
    __cabeza = Nodo

    def __init__(self):
        
        self.__cabeza = None
        
        
    
    def InsertarInmuebles(self):
        
        op = 'si'
        
        
        while op != 'NO':
            
            
            if self.__cabeza == None:
                
                localidad = input("Ingrese Localidad: ")
                direccion = input("Ingrese Direccion: ")
                superficie = float(input("Ingrese Superficie Cubierta: "))
                
                tipo = input("¿Es una Casa o Departamento? (C/D): ").upper()
                
                if tipo == 'C':
                    
                    mts_cuadrados = float(input("Ingrese Metros Cuadrados del Terreno: "))
                    
                    inmueble = Casa(localidad,direccion,superficie,mts_cuadrados)
                
                elif tipo == 'D':
                    
                    cant_departamentos = int(input("Ingrese Cantidad de Departamentos: "))
                    cant_dormitorios = int(input("Ingrese Cantidad de Dormitorios: "))
                    num_monoblock = int(input("Ingrese Numero Monoblock: "))
                    num_departamento = int(input("Ingrese Numero Departamento: "))
                    piso = int(input("Ingrese el Piso: "))
                    
                    inmueble = Departamento(localidad,direccion,superficie,cant_departamentos,
                                            cant_dormitorios,num_monoblock,num_departamento,piso)
                    
                
                nodo = Nodo(inmueble)
                self.__cabeza = nodo
            
            else:
                
                aux = self.__cabeza
                
                while aux.getSiguiente() != None:
                    
                    aux = aux.getSiguiente()
                                
                localidad = input("Ingrese Localidad: ")
                direccion = input("Ingrese Direccion: ")
                superficie = float(input("Ingrese Superficie Cubierta: "))
                
                tipo = input("¿Es una Casa o Departamento? (C/D): ").upper()
                
                if tipo == 'C':
                    
                    mts_cuadrados = float(input("Ingrese Metros Cuadrados del Terreno: "))
                    
                    inmueble = Casa(localidad,direccion,superficie,mts_cuadrados)
                
                elif tipo == 'D':
                    
                    cant_departamentos = int(input("Ingrese Cantidad de Departamentos: "))
                    cant_dormitorios = int(input("Ingrese Cantidad de Dormitorios: "))
                    num_monoblock = int(input("Ingrese Numero Monoblock: "))
                    num_departamento = int(input("Ingrese Numero Departamento: "))
                    piso = int(input("Ingrese el Piso: "))
                    
                    inmueble = Departamento(localidad,direccion,superficie,cant_departamentos,
                                            cant_dormitorios,num_monoblock,num_departamento,piso)
                    
                
                nodo = Nodo(inmueble)
                
                aux.setSiguiente(nodo)
            
            op = input("¿Insertar Otro Inmueble? (Si/No): ").upper()
            
            
    def mostrar(self):
        
        aux = self.__cabeza
        
        while aux != None:
            
            print(aux.getDato())
            
            aux = aux.getSiguiente()
    
    def mostrar_inmuebles_por_dormitorios(self,dormitorios):
        
        aux = self.__cabeza
        
        while aux != None:
            
            if isinstance(aux.getDato(),Departamento) and aux.getDato().getCantDormitorios() < dormitorios:
                
                
                print("Cantidad Departamentos: ",aux.getDato().getCantDepartamentos())
                print("Cantidad Dormitorios: ",aux.getDato().getCantDormitorios())
                print("Numero Monoblock: ",aux.getDato().getNumMonoblock())
                print("Numero Departamento: ",aux.getDato().getNumDepartamento())        
                print("Piso: ",aux.getDato().getPiso())
        
                # O 
                #print(aux.getDato())
                
                print("Importe de Venta: ", aux.getDato().importeDeVenta())
                print("\n")
            
            
            aux = aux.getSiguiente()
                    
    
    
                
                    
        
    def mostrar_inmuebles_tipo_casa(self):
        
        
        aux = self.__cabeza
        
        while aux != None:
            
            if isinstance(aux.getDato(),Casa):
                
                
                print("Direccion: ", aux.getDato().getDireccion())
                print("Superficie Cubierta:", aux.getDato().getSuperficieCubierta())
                print("Importe de Venta: ", aux.getDato().importeDeVenta())
                print("________________________________________________\n")
            
            aux = aux.getSiguiente()
    
    