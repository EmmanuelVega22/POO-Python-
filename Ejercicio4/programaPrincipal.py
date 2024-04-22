# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import csv
import os
import funciones
from Moto import Moto
from Pedidos import Pedido
if __name__ == '__main__':

    funciones.cargarMotos()
    
    funciones.cargarPedidos()

    #CARGAR NUEVOS PEDIDOS

    print("CARGAR NUEVOS PEDIDOS:")

    funciones.cargarNuevosPedidos()




