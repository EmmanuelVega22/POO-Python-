# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from menu import menu
from gestorLadrillo import GestorLadrillos
from gestorMaterial import GestorMaterial

if __name__=='__main__':
    
    gladrillo = GestorLadrillos()
    gmaterial = GestorMaterial()
    gmaterial.cargarMateriales(gladrillo)
    
    #gmaterial.mostrar()
    #print("__________________________")
    #gladrillo.mostrar()
    
    op = 0
    
    while(op != '4'):
        
        op = menu()
        
        if op == '1':
            
            identificador = input("Ingrese identificador: ")
            
            gladrillo.mostrarCostoyMaterial(identificador)
        
        elif op == '2':
            
            gladrillo.listarLadrillos()
            
        elif op == '3':
            
            gladrillo.listadoDeLadrillos()