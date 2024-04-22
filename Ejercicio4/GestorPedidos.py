# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:31:43 2024

@author: Emmanuel
"""

class GestorPedidos:
    
    __listaMotos : list

    def __init__(self):

        self.__listaMotos = []

    def getList(self):

        return self.__listaMotos
    def agregarPedido(self,newPedido):

        self.__listaMotos.append(newPedido)

