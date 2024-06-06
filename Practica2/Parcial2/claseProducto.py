# -*- coding: utf-8 -*-
"""

@author: USUARIO
"""
import abc
from abc import ABC
from datetime import datetime

class Productos(ABC):
    
    __nom_producto:str
    __fecha_envasado:str
    __fecha_vencimiento:str
    __temperatura_mantenimiento: str
    __pais_origen:str
    __numero_lote:int
    __costo_base:float
    
    def __init__(self,nom_producto,fecha_envasado,fecha_vencimiento,temperatura,
                 pais,num_lote,costo):
        
        self.__nom_producto = nom_producto
        self.__fecha_envasado = datetime.strptime(fecha_envasado,"%d/%m/%y")
        self.__fecha_vencimiento = datetime.strptime(fecha_vencimiento,"%d/%m/%y")
        self.__temperatura_mantenimiento = temperatura
        self.__pais_origen = pais
        self.__numero_lote = num_lote
        self.__costo_base = costo
     
    def __str__(self):
        
        cadena = "Producto\n"
        cadena += "Nombre Producto: " + self.__nom_producto + '\n'
        cadena += "Fecha Envasado: " + str(self.__fecha_envasado) + '\n'
        cadena += "Fecha Vencimiento: " + str(self.__fecha_vencimiento) + '\n'
        cadena += "Temperatura Matenimiento: " + self.__temperatura_mantenimiento + '\n'
        cadena += "Pais Origen: " + self.__pais_origen + '\n'
        cadena += "Numero Lote: " + str(self.__numero_lote) + '\n'
        cadena += "Costo Base: " + str(self.__costo_base) + '\n'
        
        return cadena
    
    def getNombreProducto(self):
        
        return self.__nom_producto
    
    def getFechaEnvasado(self):
        
        return self.__fecha_envasado
    
    def getFechaVencimiento(self):
        
        return self.__fecha_vencimiento
    
    def getTemperatura(self):
        
        return self.__temperatura_mantenimiento
    
    def getPaisOrigen(self):
        
        return self.__pais_origen
    
    def getNumeroLote(self):
        
        return self.__numero_lote
    
    def getCostoBase(self):
        
        return self.__costo_base
    
    
    @abc.abstractmethod
    def importeDeVenta(self):
        
        pass