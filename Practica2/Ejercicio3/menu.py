# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from colorama import init, Fore

def menu():
    
    init()

    print(Fore.RED+"**********************************************************************")
    print("*                 MENU DE OPCIONES                                            *")
    print("*******************************************************************************")
    print("* 1. Informar la duracion de todos los programa matriculados de un empleado.  *")
    print("* 2. Mostrar Empleados Matriculados en un Programa de Capacitacion.           *")
    print("* 3. Informar Empleados que no estan matriculados en ninguna programa.        *")
    print("* 4. Salir.                                                                   *")
    print("*******************************************************************************")
    op = input("\nIngrese una Opcion: ")
    
    return op