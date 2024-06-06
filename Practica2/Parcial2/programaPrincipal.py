# -*- coding: utf-8 -*-
"""
@author: USUARIO
"""
from claseGestorProductos import GestorProductos
from menu import menu

if __name__ == '__main__':
    
    gestor = GestorProductos()
    
    gestor.cargarLista()
    gestor.mostrarProductos()
    op = 0

    while op != '5':
        
        op = menu()
        
        if op == '1':
            
            gestor.insertarProducto()
            
        elif op == '2':
            
            posicion = int(input("Ingrese una posicion: "))
            
            gestor.mostrarPorPosicion(posicion-1)
        
        elif op == '3':
            
            gestor.cantidadDeTipoProductos()
        
        elif op == '4':
            
            gestor.productos()
    