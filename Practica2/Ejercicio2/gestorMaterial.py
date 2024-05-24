# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseMaterial import Material

class GestorMaterial:
    
    __listMateriales : list
    
    def __init__(self):
        
        self.__listMateriales = []
        
    
    def agregarMaterial(self,nuevoMaterial):
        
        self.__listMateriales.append(nuevoMaterial)
        
    def cargarMateriales(self,gladrillos):
        
        
        op = input("Cargar Materiales ('Si' o 'No'):\n")
        
        while op.lower() == 'si':
            
            print(" __________________________")
            print("|                          |")
            print("|   Cargar Materiales      |")
            print("|__________________________|")
            material = input("Ingrese Material: ")
            caracteristicas = input("Ingrese Caracteristicas: ")
            
            while True:
               
                try:
                    
                    cant_util = int(input("Ingrese Cantidad de Material Utilizado: "))
                    cost_adic = float(input("Ingrese Costo Adicional: "))
                    break
                
                except ValueError: #Operación sobre un objeto de tipo correcto pero valor inapropiado
                    
                    print("Por favor, ingrese un número válido para la cantidad y/o el costo.")
        
            
            nuevoMaterial = Material(material,caracteristicas,cant_util,cost_adic)
            
            try:
                
                gladrillos.cargarLadrillos(nuevoMaterial)
                
            except Exception as e:
                print(f"Error al cargar ladrillos: {e}")
            
            self.agregarMaterial(nuevoMaterial)
            
            op = input("Cargar Otro Materiales ('Si' o 'No')?\n")
            
    def mostrar(self):    
        
        for i in range(len(self.__listMateriales)):
                
            print(self.__listMateriales[i])