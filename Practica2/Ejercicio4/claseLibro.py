
from clasePublicaciones import Publicaciones
from datetime import datetime

class Libro(Publicaciones):

    __nombre_autor: str
    __fecha_edicion: str
    __cant_paginas: int


    def __init__(self,titulo,categoria,precio_base,autor,fecha,paginas):

        super().__init__(titulo,categoria,precio_base)

        self.__nombre_autor = autor
        self.__fecha_edicion = fecha
        self.__cant_paginas = paginas

    def __str__(self):
        
        cadena = super().__str__()
        cadena += 'Libro:\n'
        cadena += 'Autor:'+ (self.__nombre_autor)+'\n'
        cadena += 'Fecha:'+(self.__fecha_edicion)+'\n'
        cadena += 'Paginas:'+str(self.__cant_paginas)+'\n'

        return cadena

    def getAutor(self):

        return self.__nombre_autor
    
    def getFechaEdicion(self):

        return self.__fecha_edicion

    def getPaginas(self):

        return self.__cant_paginas
    
    def importeVenta(self):
        
        antiguedad =  int(datetime.now().year) - int(self.getFechaEdicion())

        descuento = antiguedad * 0.001

        importeVenta = self.getPrecioBase() - (self.getPrecioBase() * descuento)

        return importeVenta