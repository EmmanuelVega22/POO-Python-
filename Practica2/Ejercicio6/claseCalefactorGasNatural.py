# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseCalefactor import Calefactor

class CalefactorGasNatural(Calefactor):
    
    __matricula:str
    __calorias: str
    
    def __init__(self,marca,modelo,paisFabricacion,precio,formaPago,cuotas,matricula,calorias):
        
        super().__init__(marca,modelo,paisFabricacion,precio,formaPago,cuotas)
        
        self.__matricula = matricula
        self.__calorias = calorias
        
    
    def __str__(self):
        
        cadena = super().__str__()
        
        cadena += 'Tipo GasNatural:\n'
        cadena += 'Matricula: ' + self.__matricula + '\n'
        cadena += 'Calorias: ' + self.__calorias + '\n'
        return cadena
    
    def getMatricula(self):
        
        return self.__matricula
    
    def getCalorias(self):
        
        return self.__calorias
    
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
                        matricula = self.__matricula,
                        calorias = self.__calorias
                        )
                )
        return d
    
    def importeDeVenta(self):
        
        pass