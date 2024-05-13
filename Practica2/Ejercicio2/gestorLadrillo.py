# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseLadrillo import Ladrillo

class GestorLadrillos:
    
    __listLadrillos : list
    
    
    def __init__(self):
        
        self.__listLadrillos = []
        
    def agregarLadrillos(self,nuevoLadrillo):
        
        self.__listLadrillos.append(nuevoLadrillo)
        
    
    def cargarLadrillos(self,material):
        
        print(" __________________________")
        print("|                          |")
        print("|     Cargar Ladrillos     |")
        print("|__________________________|")
        identificador = input("Identificador: ")
        
        while True:
               
                try:
                    
                    cantidad = int(input("Cantidad de Ladrillos: "))
                    materialUtilizado = float(input("Kg de Material Utilizado: "))
                    costo = float(input("Costo: "))
                    break
                
                except ValueError: #Operación sobre un objeto de tipo correcto pero valor inapropiado
                    
                    print("Por favor, ingrese un número válido para la cantidad,materialUtilizado y/o costo.")
        
        
        nuevoLadrillo = Ladrillo(cantidad,identificador,materialUtilizado,costo,material)
        
        self.agregarLadrillos(nuevoLadrillo)
    
    def mostrar(self):    
        
        for i in range(len(self.__listLadrillos)):
                
            print(self.__listLadrillos[i])
        
    def mostrarCostoyMaterial(self,identificador):
        
        i =0
        
        while i < len(self.__listLadrillos) and self.__listLadrillos[i].getIdentificador() != identificador:
            
            i+=1
        
        if self.__listLadrillos[i].getIdentificador() == identificador:
            
            
            print("Ladrillo: ",self.__listLadrillos[i].getIdentificador())
            print("Caracteristica: ",self.__listLadrillos[i].caracteristicaDelLadrillo())
            print("Costo: ",self.__listLadrillos[i].getCosto())
        
        
    def listarLadrillos(self):
        
        for i in range(len(self.__listLadrillos)):
            
            print("Ladrillo de: ", self.__listLadrillos[i].materialDelLadrillo())
            print("Costo de Fabricacion: $", self.__listLadrillos[i].costoDeFabricacion())
            print("__________________________")
            
    def listadoDeLadrillos(self):
        
        for i in range(len(self.__listLadrillos)):
            
            print("NºIdentificador\t\tMaterial\t\tCosto Asociado\n")
            print("{}\t\t\t{}\t\t\t{}\n".format(self.__listLadrillos[i].getIdentificador(),self.__listLadrillos[i].materialDelLadrillo(),self.__listLadrillos[i].costoDeFabricacion()))