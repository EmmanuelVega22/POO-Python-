# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Pedido:
    
    __patente = str
    __idPedido = str
    __comida = str
    __tiempoEstimado = str
    __tiempoRealEstimado = str
    __importe = float

    def __init__(self,patente,idPedido,comida,tiempoEst,tiempoRealEst,importe):
        
        self.__patente = patente
        self.__idPedido = idPedido
        self.__comida = comida
        self.__tiempoEstimado = tiempoEst
        self.__tiempoRealEstimado = tiempoRealEst
        self.__importe = importe
        


    def getPedido(self):

        return self.__listPedido
    
    def getPatente(self):

        return self.__patente