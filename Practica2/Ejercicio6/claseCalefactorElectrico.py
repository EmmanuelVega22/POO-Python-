# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    
    __potencia_maxima:str
    
    
    def __init__(self,marca,modelo,paisFabricacion,precio,formaPago,cuotas,potenciaMaxima):
        
        super().__init__(marca,modelo,paisFabricacion,precio,formaPago,cuotas)
        
        self.__potencia_maxima = potenciaMaxima
        
    
    def __str__(self):
        
        cadena = super().__str__()
        
        cadena += 'Tipo Electrico:\n'
        cadena += 'Potencia Maxima: ' + self.__potencia_maxima + '\n'
        
        return cadena
    
    def getPotenciaMaxima(self):
        
        return self.__potencia_maxima
    
    def toJSON(self):
        
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                        marca = self.getMarca(),
                        modelo = self.getModelo(),
                        paisFabricacion = self.getPaisFabricacion(),
                        precio = self.getPrecio(),
                        formaPago = self.getFormaPago(),
                        cuotas = self.getCuotas(),
                        potenciaMaxima = self.__potencia_maxima
                        )
                )
        return d
    
    def importeDeVenta(self):
        
        pass