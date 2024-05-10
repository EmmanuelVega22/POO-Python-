# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

import csv
from claseTransacciones import Transacciones

class GestorTransacciones:
    
    __listTransacciones: list
    
    
    def __init__(self):
        
        self.__listTransacciones = []
        
        
     
    def agregarTransacciones(self,nuevaTransaccion):
        
        self.__listTransacciones.append(nuevaTransaccion)
        
    
    def cargarTransacciones(self):
        
        archiTransacciones = open('transaccionesBilletera.csv')
        readerTransacciones = csv.reader(archiTransacciones,delimiter=',') 
        
        for fila in readerTransacciones:
     
            nuevaTransaccion = Transacciones(fila[0],fila[1],fila[2],fila[3])
                
            self.agregarTransacciones(nuevaTransaccion)
                
    def mostrar(self):
        
        for i in range(len(self.__listTransacciones)):
            
            print(self.__listTransacciones[i])
            
            
    def buscarTransacciones(self, cvu,saldo):
        
        i = 0
        
        while i < len(self.__listTransacciones):
            
            if self.__listTransacciones[i].getCVU() == cvu:

                if self.__listTransacciones[i].getTipo_transaccion() == 'D':
                    
                    saldo = saldo - self.__listTransacciones[i].getImporte()
                
                elif self.__listTransacciones[i].getTipo_transaccion() == 'C':
                    
                    saldo = saldo + self.__listTransacciones[i].getImporte()
            
            i = i+1
        
        return saldo
        