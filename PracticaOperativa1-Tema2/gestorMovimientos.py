# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import numpy as np
import csv
from claseMovimientos import Movimientos

class GestorMovimientos:
    
    __arregloMovimientos : np.array
    
    
    def __init__(self):
        
        self.__arregloMovimientos = np.array([])
        
    
    def agregarMovimientos(self,nuevoMovimiento):
        
        #self.__arregloMovimientos = np.array(nuevoMovimiento)
        self.__arregloMovimientos = np.append(self.__arregloMovimientos, nuevoMovimiento)

    
    def cargarMovimientos(self):
        
        archivoMovimientos = open('MovimientosAbril2024.csv', mode ='r', newline='')
        readerMovimientos = csv.reader(archivoMovimientos,delimiter =';')
        
        next(readerMovimientos)
        # Omite la primera línea porque en el archivo.csv la primer linea tiene el nombre de las columnas

        for fila in readerMovimientos:
            
            nuevoMovimiento = Movimientos(fila[0],fila[1],fila[2],fila[3],fila[4])
            
            self.agregarMovimientos(nuevoMovimiento)
        
        archivoMovimientos.close()
   
    def mostrar(self):

        for i in range(len(self.__arregloMovimientos)):
            
            print(self.__arregloMovimientos[i])
            
    
    def buscarMovimientos(self,nroCuenta,saldo):
        
        i = 0
        
        while i < len(self.__arregloMovimientos):
            
            
            if self.__arregloMovimientos[i].getNroCuenta() == nroCuenta:
                
                print("{}\t\t{}\t\t{}\t\t{}".format(self.__arregloMovimientos[i].getFecha(),self.__arregloMovimientos[i].getDescripcion(),self.__arregloMovimientos[i].getImporte(),self.__arregloMovimientos[i].getTipoMovimiento()))
                
                if self.__arregloMovimientos[i].getTipoMovimiento() == 'C':
                    
                    saldo = saldo - float(self.__arregloMovimientos[i].getImporte())
                
                elif self.__arregloMovimientos[i].getTipoMovimiento() == 'P':
                    
                    saldo = saldo + float(self.__arregloMovimientos[i].getImporte())
            
            i = i+1
        
        return saldo
    
    