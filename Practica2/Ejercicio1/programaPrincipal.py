# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from funciones import menu
from gestorEdificios import GestorEdificios


if __name__=='__main__':
    
    gedificios = GestorEdificios()
    op = 0
    
    gedificios.cargarEdificios()
    #gedificios.mostrar()    
    
    while(op != '5'):
        
        op = menu()
        
        if op == '1':
            
            nombre = input("Ingrese Nombre del Edificio: ")
            
            gedificios.buscarPropietarios(nombre)
        
        elif op == '2':
            gedificios.mostrarSuperficieTotalCubierta()
        
        elif op == '3':
            
            nombre_propietario = input("Ingrese Nombre del Propietario:")
            gedificios.SuperficieTotalCubiertaDeUnPropietario(nombre_propietario)
        
        elif op == '4':
            
            num_piso = int(input("Ingrese Numero de un Piso:"))
            gedificios.mostrarPisos(num_piso)
    
    