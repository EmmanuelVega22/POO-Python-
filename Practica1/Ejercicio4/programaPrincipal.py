# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

import msvcrt #Pausar pantalla
import os #limpiar pantalla

from GestorPedidos import GestorPedidos
from GestorMotos import GestorMotos

if __name__ == '__main__':

    
    gpedidos = GestorPedidos()
    
    gmotos = GestorMotos()
    
    
    gpedidos.cargarArchivoPedidos()
    print("Archivo Pedidos")
    print("______________")
    gpedidos.mostrar()
    print("______________")
    print("Archivo Motos")
    print("______________")
    gmotos.cargarArchivoMotos()
    gmotos.mostrar()
    gpedidos.ordenarListPedidos()
    
    print("_____________________")
    print("|AGREGAR NUEVO PEDIDO|")
    print("|____________________|")
    
    patente = input("Ingrese Patente de la Moto: ")
    
    if gmotos.buscarPatente(patente) != False:
        
        gpedidos.cargarNuevosPedidos(gmotos.buscarPatente(patente))
    
    msvcrt.getch()
    os.system('cls')
    gpedidos.mostrar()
    print("___________________________________")
    gpedidos.ordenarListPedidos()
    gpedidos.mostrar()
    msvcrt.getch()
    os.system('cls')
    print(" __________________________________")
    print("|MODIFICAR TIEMPO REAL DE UN PEDIDO|")
    print("|__________________________________|")
    
    gpedidos.modificarPedido()
    msvcrt.getch()
    os.system('cls')
    
    print(" __________________________________________________")
    print("|MOSTRAR DATOS DE UNA MOTO Y SU PROMEDIO DE ENTREGA|")
    print("|__________________________________________________|")
    
    patente =input("Ingrese Patente de la Moto: ")
    
    gmotos.mostrarDatosMoto(patente,gpedidos.buscarPedidosPorPatente(patente))
    msvcrt.getch()

    print(" _____________________________________________")
    print("|LISTADO DE MOTOS,CONDUCTORES Y SUS COMISIONES|")
    print("|_____________________________________________|")
    
    gmotos.listadoMotos(gpedidos)
    msvcrt.getch()
