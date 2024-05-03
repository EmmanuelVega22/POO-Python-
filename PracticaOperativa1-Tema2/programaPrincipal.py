# -*- coding: utf-8 -*-
"""

@author: Emmanuel
"""
import funcionesM
from gestorClientes import GestorClientes
from gestorMovimientos import GestorMovimientos

if __name__=='__main__':
    
    gclientes = GestorClientes()
    gmovimientos = GestorMovimientos()
    
    gclientes.cargarClientes()
    gmovimientos.cargarMovimientos()
    
    
    op = 0
    
    while op!= '4':
        
        op = funcionesM.menu()
        
        if op == '1':
            
            dni = input("Ingrese Dni del Cliente: ")
            
            gclientes.listadoClientePorDni(dni,gmovimientos)
        
        elif op == '2':
            
            dni = input("Ingrese Dni del Cliente: ")
            
            gclientes.movimientosDelCliente(dni,gmovimientos)
            
        elif op == '3':
            
            gclientes.ordenarListaClientes()
            gclientes.mostrar()