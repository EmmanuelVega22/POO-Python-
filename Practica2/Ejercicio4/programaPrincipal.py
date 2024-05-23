# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from menu import menu
from claseColeccionLista import ColeccionLista
from datetime import datetime

if __name__ == '__main__':
    
    
    clista = ColeccionLista()
        
    
    op = 0
    
    while op != '5':
        
        op = menu()
        
        if op == '1':
            
            clista.cargarColeccionLista()
        
        elif op == '2':
        
            posicion = int(input("Ingrese una posicion: "))
            
            clista.mostrar_tipo_publicacion(posicion)
        
        elif op == '3':
            
            clista.mostrar_cantidad_publicaciones()
        
        elif op == '4':
            
            clista.mostrar_publicaciones()
    