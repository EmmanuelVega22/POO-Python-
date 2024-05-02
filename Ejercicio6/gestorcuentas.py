# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

import csv
import numpy as np
from claseCuenta import Cuenta

class GestorCuentas:
    
    __arregloCuentas: np.ndarray
    
    
    def __init__(self):
        
        self.__arregloCuentas = np.array([])
    
    
    def agregarCuentas(self,nuevaCuenta):
        
        self.__arregloCuentas = np.append(self.__arregloCuentas, nuevaCuenta)
    
    
    def cargarCuentas(self):
        
        archiCuentas = open('cuentasBilleteras.csv')
        readerCuentas = csv.reader(archiCuentas,delimiter=',') 
        
        for fila in readerCuentas:
                
            nuevaCuenta = Cuenta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                
            self.agregarCuentas(nuevaCuenta)
             
    def mostrar(self):
        
        for i in range(len(self.__arregloCuentas)):
            
            print(self.__arregloCuentas[i])
            
    
    def listadoDatosCliente(self,dni,gtransaccion):
        
        i = 0
        
        while i < len(self.__arregloCuentas):
            
            if self.__arregloCuentas[i].getDni() == dni:
            
                
                self.__arregloCuentas[i].setSaldo(gtransaccion.buscarTransacciones(self.__arregloCuentas[i].getCVU(),self.__arregloCuentas[i].getSaldo()))

                print("Cliente: {} {}".format(self.__arregloCuentas[i].getNombre(),self.__arregloCuentas[i].getApellido()))
                
                print("DNI: ",self.__arregloCuentas[i].getDni())
                print("CVU: ", self.__arregloCuentas[i].getCVU())
    
                print("Saldo(Actualizado): ", self.__arregloCuentas[i].getSaldo())
                
                break
            
            i = i+1
            
    def ModificarPorcentajeAnual(cls):
        
        
        nuevoPorcentaje = input("Ingrese el Nuevo Porcentaje anual: ")
        
        cls.__arregloCuentas[0].setPorcentajeAnual(nuevoPorcentaje)
        
    
    def ActualizarSaldos(self):
        
        
        for i in range(len(self.__arregloCuentas)):
            
            self.__arregloCuentas[i].setSaldo(self.__arregloCuentas[i].getSaldo() + self.__arregloCuentas[i].getSaldo()*round(self.__arregloCuentas[i].getPorcentajeAnual()/365,2))
        
        self.mostrar()
    
    def InformarNuevoSaldo(self,gtransaccion,cvu):
        
        i = 0
        
        while i < len(self.__arregloCuentas) and self.__arregloCuentas[i].getCVU() != cvu:
                
            i = i+1
            
        
        if self.__arregloCuentas[i].getCVU() == cvu:
            
            print("Saldo Inicial: $",self.__arregloCuentas[i].getSaldo())
                    
            self.__arregloCuentas[i].setSaldo(gtransaccion.buscarTransacciones(self.__arregloCuentas[i].getCVU(),self.__arregloCuentas[i].getSaldo()))
            
            print("Nuevo Saldo Inicial (Actualizado): $",self.__arregloCuentas[i].getSaldo())
            
        else: print("No existe ese CVU!")
        
    
    def ActualizarDatosEnUnArchivo(self):
        
        nombre_archivo = 'nuevasCuentasBilleteras.csv'
        
        try: 
            # Intenta abrir el archivo CSV en modo lectura
            #Para verificar si existe,Si existe lo actualiza con los nuevos datos
            with open(nombre_archivo, 'r', newline='') as nuevo_archivo_lectura: #Archivo Abierto para Lectura
                readerCuentas = csv.reader(nuevo_archivo_lectura)
                datos_del_archivo = list(readerCuentas)  # Leer los datos del archivo csv y lo convierte en una lista
            
            # Método para obtener los atributos de las Cuentas como una lista
            datos_nuevos_lista = [cuenta.obtener_datos_como_lista() for cuenta in self.__arregloCuentas]
            
            # Modificar los datos originales con los datos actualizados de la lista
            for i,fila in enumerate(datos_del_archivo):
                datos_del_archivo[i] = datos_nuevos_lista[i]  #Modifica toda una linea del archivo con un bloque completo de la lista
            
            # Escribir los datos actualizados de vuelta al archivo csv
            with open(nombre_archivo, 'w', newline='') as nuevo_archivo_escritura:#Archivo Abirto para Escritura
                writerEquipo = csv.writer(nuevo_archivo_escritura)
                writerEquipo.writerows(datos_del_archivo)
                
        except FileNotFoundError:# Si el archivo no existe, se crea uno nuevo
            
            # Método para obtener los atributos de las Cuentas como una lista
            datos_nuevos_lista = [cuenta.obtener_datos_como_lista() for cuenta in self.__arregloCuentas]
            
            # Escribir los datos actualizados en el nuevo archivo csv
            with open(nombre_archivo, 'w', newline='') as nuevo_archivo_csv:#Archivo Abirto para Escritura
                writerEquipo = csv.writer(nuevo_archivo_csv)
                writerEquipo.writerows(datos_nuevos_lista)