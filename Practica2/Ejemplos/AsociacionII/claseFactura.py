# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Factura:
    __numeroFactura: str
    __fecha: object
    __importe: float
    __cuit: str
    __denominacionNegocio: str
    __descuento: float
    
    def __init__(self, numeroFactura,fecha, importe, cuit, denominacionNegocio):

        self.__numeroFactura=numeroFactura
        self.__fecha=fecha
        self.__importe=importe
        self.__cuit=cuit
        self.__denominacionNegocio=denominacionNegocio
        
        if self.__importe>2500:
            self.__descuento=250
        
        else:
            self.__descuento=100
    
    def getTotal(self):
        
        return self.__importe-self.__descuento
    
    def getNumeroFactura(self):
        return self.__numeroFactura