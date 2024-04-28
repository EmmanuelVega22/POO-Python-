# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Pedido:
    
    __patenteMoto: str
    __idPedido: str
    __comidaPedida : str
    __tiempoEstimado: int
    __tiempoRealEntrega: int
    __precio: float
    
    def __init__(self,patente,idPedido,comidaPedida,tiempoEst,tiempoRealEnt,precio):
        
        self.__patenteMoto = patente
        self.__idPedido =idPedido
        self.__comidaPedida = comidaPedida
        self.__tiempoEstimado = tiempoEst
        self.__tiempoRealEntrega = tiempoRealEnt
        self.__precio = precio
    
    
    def __str__(self):
        
        return "%s %s %s %s %s %s" % (self.__patenteMoto, self.__idPedido, self.__comidaPedida, self.__tiempoEstimado, self.__tiempoRealEntrega,self.__precio)
   
    def getPatenteMoto(self):
        
        return self.__patenteMoto
    
    def getidPedido(self):
        
        return self.__idPedido
    
    def getTiempoRealEntrega(self):
        
        return self.__tiempoRealEntrega
    
    def setTiempoRealEntrega(self,nuevoTiempo):
        
        self.__tiempoRealEntrega = nuevoTiempo
        
    def getTiempoEstimado(self):
        
        return self.__tiempoEstimado
    
    def getPrecio(self):
        
        return self.__precio