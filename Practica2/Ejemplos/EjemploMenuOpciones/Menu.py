# -*- coding: utf-8 -*-
"""

@author: Emmanuel
"""
import msvcrt
from colorama import init, Fore #Instalar 'pip install colorama'
#from termcolor import colored #Instalar 'pip install termcolor

def print_menu():
    
    init()

    print(Fore.RED + "***************************************************")
    print("*                 MENU DE OPCIONES                *")
    print("***************************************************")
    print("* 1. Realizar un préstamo                         *")
    print("* 2. Agregar un nuevo socio                       *")
    print("* 3. Actualizar información                       *")
    print("* 4. Generar un informe                           *")
    print("* 5. Ver lista de libros                          *")
    print("* 6. Salir                                        *")
    print("***************************************************")
    
print_menu()
msvcrt.getch()
