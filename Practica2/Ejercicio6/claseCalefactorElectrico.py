# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    
    __potencia_maxima = str
    
    
    def __init__(self,marca,modelo,pais,precio,forma_pago,cant_cuotas,potencia):
        
        super().__init__(marca,modelo,pais,precio,forma_pago,cant_cuotas)
        
        self.__potencia_maxima = potencia

    def __str__(self):
        
        cadena = super().__str__()
        cadena += 'Potencia Maxima: ' + self.__potencia_maxima + '\n'
        
        return cadena
        
    def getPotenciaMaxima(self):
        
        return self.__potencia_maxima
    
    def importeDeVenta(self):
        
        pass
    
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                        x=self.__x,
                        y=self.__y
                        )
                )
        return d