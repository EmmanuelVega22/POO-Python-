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
    print("* 1. Motrar Nombre y Apellido de cada uno de los Propietarios.                *")
    print("* 2. Mostrar Superficie Total del Edificio.                                   *")
    print("* 3. Mostrar la superficie total cubierta del departamento.                   *")
    print("* 4. Mostrar y Contar la cantidad de departamentos que tienen 3dorm y 1 baño. *")
    print("* 5. Salir.                                                                   *")
    print("*******************************************************************************")
    op = input("\nIngrese una Opcion: ")
    
    return op