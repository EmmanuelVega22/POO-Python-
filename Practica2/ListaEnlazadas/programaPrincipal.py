# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from menu import menu
from claseLista import Lista
from claseProfesor import Profesor
if __name__=='__main__':

    nuevaLista = Lista()
    
    op = 0
    
    while op != '4':
        
        op = menu()
        
        if op == '1':
            
            print("Cargar Profesores:\n")
            
            nombre = input("Ingrese Nombre de un Profesor: ")
            
            while nombre.lower() != 'fin':
                
                apellido = input("Ingrese Apellido: ")
                dni = int(input("Ingrese DNI: "))
                puesto = input("Ingrese Puesto: ")
                
                nuevoProfesor = Profesor(dni,nombre,apellido,puesto)
                nuevaLista.agregarProfesorPorCabeza(nuevoProfesor)
                #nuevaLista.agregarProfesorPorCola(nuevoProfesor)

                nombre = input("Ingrese otro Nombre de un Profesor ('Fin' para terminar): ")
        
        if op == '2':
            
            nuevaLista.listarDatosProfesores()
            
        if op == '3':
            
            dni = int(input("Ingrese DNI del profesor que desea eliminar: "))
            nuevaLista.eliminarPorDNI(dni)