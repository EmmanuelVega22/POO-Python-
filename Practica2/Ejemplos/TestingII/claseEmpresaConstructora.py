# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import abc
from abc import ABC

class EmpresaConstructora(ABC):
    
    __localidad: str
    __direccion: str
    __superficie_cub: float
    
    
    def __init__(self,localidad,direccion,superficie):
        
        self.__localidad = localidad
        self.__direccion = direccion
        self.__superficie_cub = superficie
        
    
    def __str__(self):
        
        cadena = 'Inmueble:\n'
        cadena += 'Localidad: ' + self.__localidad + '\n'
        cadena += 'Direccion: ' + self.__direccion + '\n'
        cadena += 'Superficie Cubierta: ' + str(self.__superficie_cub) + '\n'
        
        return cadena
    
    def getLocalidad(self):
        
        return self.__localidad
    
    def getDireccion(self):
        
        return self.__direccion
    
    def getSuperficieCubierta(self):
        
        return self.__superficie_cub
    
    @abc.abstractmethod
    def importeDeVenta(self):
        
        pass
        
    