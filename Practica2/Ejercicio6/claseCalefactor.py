# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:07:24 2024

@author: Emmanuel
"""
import abc
from abc import ABC

class Calefactor(ABC):
    
    __marca: str
    __modelo: str
    __pais_fabricacion: str
    __precio_lista: float
    __forma_pago: str
    __cant_cuotas: int
    
    def __init__(self,marca,modelo,paisFabricacion,precio,formaPago,cuotas):
        
        self.__marca = marca
        self.__modelo = modelo
        self.__pais_fabricacion = paisFabricacion
        self.__precio_lista = precio
        self.__forma_pago = formaPago
        self.__cant_cuotas = cuotas
        
        
    def __str__(self):
        
        cadena = 'Calefactor:\n'
        cadena += 'Marca: ' + self.__marca + '\n'
        cadena += 'Modelo: ' + self.__modelo + '\n'
        cadena += 'Pais Fabricacion: ' + self.__pais_fabricacion + '\n'
        cadena += 'Precio Lista: ' + str(self.__precio_lista) + '\n'
        cadena += 'Forma Pago: ' + self.__forma_pago + '\n'
        cadena += 'Cantidad Cuotas: ' + str(self.__cant_cuotas) + '\n'
        
        return cadena
    
    def getMarca(self):
        
        return self.__marca
    
    def getModelo(self):
        
        return self.__modelo
    
    def getPaisFabricacion(self):
        
        return self.__pais_fabricacion
    
    def getPrecio(self):
        
        return self.__precio_lista
    
    def getFormaPago(self):
        
        return self.__forma_pago
    
    def getCuotas(self):
        
        return self.__cant_cuotas
    
       
    @abc.abstractmethod
    def importeDeVenta(self):
        
        pass
       
    def toJSON(self):
        
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                        marca = self.__marca,
                        modelo = self.__modelo,
                        pais = self.__pais_fabricacion,
                        precio = self.__precio_lista,
                        forma_pago = self.__forma_pago,
                        cuotas = self.__cant_cuotas
                        )
                )
        return d