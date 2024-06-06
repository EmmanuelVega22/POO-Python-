# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseCalefactor import Calefactor

class CalefactorGasNatural(Calefactor):
    
    __matricula: str
    __calorias: str
    
    
    def __init__(self,marca,modelo,pais,precio,forma_pago,cant_cuotas,matricula,calorias):
        
        super().__init__(marca,modelo,pais,precio,forma_pago,cant_cuotas,matricula,calorias)
        
        self.__matricula = matricula
        self.__calorias = calorias
        
    
    def __str__(self):
        
        cadena = super().__str__()
        
        cadena += 'Matricula: ' + self.__matricula + '\n'
        cadena += 'Calorias: ' + self.__calorias + '\n'
        
        return cadena
    
    
    def getMatricula(self):
        
        return self.__matricula
    
    def getCalorias(self):
        
        return self.__calorias
    
    def importeDeVenta(self):
        
        pass
        
        
