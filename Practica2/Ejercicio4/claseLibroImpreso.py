# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from datetime import datetime


from clasePublicaciones import Publicaciones

class LibroImpreso(Publicaciones):
    
    __nombre_autor: str
    __fecha_edicion: str
    __cant_pag: int
    
    def __init__(self,titulo,categoria,precio,autor,fecha,paginas):
        
        super().__init__(titulo,categoria,precio)
        
        self.__nombre_autor = autor
        self.__fecha_edicion = fecha
        self.__cant_pag = paginas
        
    def __str__(self):
        
        cadena = 'Libro:\n'
        cadena += 'Autor: '+self.__nombre_autor+'\n'
        cadena += 'Fecha Edicion: '+self.__fecha_edicion+'\n'
        cadena += 'Cantidad Paginas: '+str(self.__cant_pag)+'\n'
        return cadena
        
    def getAutor(self):
        
        return self.__nombre_autor
    
    def getFechaEdicion(self):
        
        return self.__fecha_edicion
    
    def getPaginas(self):
        
        return self.__cant_pag
    
    
    def importeDeVenta(self):
        
        antiguedad = int(datetime.now().year)-int(self.getFechaEdicion())
        
        if antiguedad < 0:
            
            raise ValueError("El año de edicion no puede ser mayor que el año actual!")
        
        descuento = antiguedad * 0.01
        
        importeVenta = self.getPrecioBase() - (self.getPrecioBase() * descuento)
        
        return importeVenta
    
        
