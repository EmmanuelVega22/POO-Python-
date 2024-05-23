# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from clasePublicaciones import Publicaciones

class CD(Publicaciones):
    
    __tiempo_reproduccion: int #minutos
    __nombre_narrador: str
    
    
    def __init__(self,titulo,categoria,precio,tiempo_reprod,narrador):
        
        super().__init__(titulo,categoria,precio)
        
        self.__tiempo_reproduccion = tiempo_reprod
        self.__nombre_narrador = narrador
        
    def __str__(self):
        
        cadena = 'CD:\n'
        cadena += 'Tiempo Reproduccion: '+str(self.__tiempo_reproduccion)+'min\n'
        cadena += 'Narrador: '+self.__nombre_narrador+'\n'
        return cadena
           
    def getTiempoReproduccion(self):
        
        return self.__tiempo_reproduccion
    
    def getNarrador(self):
        
        return self.__nombre_narrador
    
    
    def importeDeVenta(self):
        
        importeVenta = self.getPrecioBase() + (self.getPrecioBase() * 0.10)
        
        return importeVenta