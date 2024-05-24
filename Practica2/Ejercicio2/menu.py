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
    print("* 1. Detallar costo y característica del material solicitado.                 *")
    print("* 2. Mostrar para cada ladrillo el costo total de fabricación del pedido.     *")
    print("* 3. Listado Ladrillo Fabricados.                                             *")
    print("* 4. Salir.                                                                   *")
    print("*******************************************************************************")
    op = input("\nIngrese una Opcion: ")
    
    return op