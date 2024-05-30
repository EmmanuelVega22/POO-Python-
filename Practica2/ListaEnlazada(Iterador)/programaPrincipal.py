# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from menu import menu
from claseLista import Lista

if __name__=='__main__':

    nuevaLista = Lista()
    
    op = 0
    
    while op != '4':
        
        op = menu()
        
        if op == '1':
            
            print("Cargar Profesores:")
        
            nuevaLista.cargarProfesores()
        if op == '2':
            
            for dato in nuevaLista:
                
                print('Dato del',dato)
            
        if op == '3':
            
            dni = int(input("Ingrese DNI del profesor que desea eliminar: "))
            nuevaLista.eliminarProfesorPorDni(dni)