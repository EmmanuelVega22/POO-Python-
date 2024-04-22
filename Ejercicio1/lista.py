# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:39:13 2024

@author: Emmanuel
"""

from clase import CajaDeAhorro

class Lista:
    
    __cuentas: list
    
    
    def __init__(self):
        
        self.__cuentas = []
        
    def agregarCuentas(self,nuevaCuenta):
        
        self.__cuentas.append(nuevaCuenta)
      
    def testCuentas():
        
        c1 = CajaDeAhorro(1001,'Mario','Lopez','12345',500)
        c2 = CajaDeAhorro(1002,'Juan','Perez','45678',600)
        c3 = CajaDeAhorro(1003,'Ana','Maria','54321',700)
        c4 = CajaDeAhorro(1004,'Felipe','Gonzales','98765',800)
        
        Lista.agregarCuentas(c1)
        Lista.agregarCuentas(c2)
        Lista.agregarCuentas(c3)
        Lista.agregarCuentas(c4)
           
      
    def getUnaCuenta(self,indice):
        
        return self.__cuentas[indice]
    
    