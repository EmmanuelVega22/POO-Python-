# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import abc
from abc import ABC

class Publicaciones(ABC):
    
    __titulo: str
    __categoria:str
    __precio_base: float
    
    def __init__(self,titulo,categoria,precio_base):
        
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precio_base = precio_base
    
    def __str__(self):
        
        cadena = 'Publicacion:\n'
        cadena += 'Titulo: '+self.__titulo+'\n'
        cadena += 'Categoria: '+self.__categoria+'\n'
        cadena += 'Precio Base: '+self.__precio_base+'\n'
        return cadena
    
    def getTitulo(self):
        
        return self.__titulo
    
    def getCategoria(self):
        
        return self.__categoria
    
    def getPrecioBase(self):
        
        return self.__precio_base
    
    @abc.abstractmethod
    def importeDeVenta(self):
        
        pass