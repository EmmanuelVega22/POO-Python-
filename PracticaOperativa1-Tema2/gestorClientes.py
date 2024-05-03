# -*- coding: utf-8 -*-
"""

@author: Emmanuel
"""
import csv
from claseCliente import Clientes

class GestorClientes:
    
    __listClientes : list
    
    
    def __init__(self):
        
        self.__listClientes =[]
        
    def agregarClientes(self,nuevoCliente):
        
        self.__listClientes.append(nuevoCliente)
        
    
    def cargarClientes(self):
        
        archivoCliente = open('ClientesAbril2024.csv', mode= 'r', newline = '')
        readerCliente = csv.reader(archivoCliente, delimiter=';')
        
        next(readerCliente)
        # Omite la primera línea porque en el archivo.csv la primer linea tiene el nombre de las columnas


        for fila in readerCliente:
            
            nuevoCliente = Clientes(fila[0],fila[1],fila[2],fila[3],fila[4])
            
            self.agregarClientes(nuevoCliente)
            
        archivoCliente.close()
        
    def mostrar(self):
        
        
        for i in range(len(self.__listClientes)):
            
            print(self.__listClientes[i])
    
    def listadoClientePorDni(self,dni,gmovimientos):
        
        i = 0
        
        while i < len(self.__listClientes) and self.__listClientes[i].getDni() != dni:
            
            i = i+1
        
        
        if self.__listClientes[i].getDni() == dni:
            
            print("Cliente: {} {}\t\t\tNumero Cuenta:{}".format(self.__listClientes[i].getNombre(),self.__listClientes[i].getApellido(),self.__listClientes[i].getNroCuenta()))
            print("Saldo Anterior:", self.__listClientes[i].getSaldo())
            print("Movimientos")
            print("Fechas\t\tDescripcion\t\t\tImporte\t\tTipoMovimiento")
            
            nuevoSaldo = gmovimientos.buscarMovimientos(self.__listClientes[i].getNroCuenta(),float(self.__listClientes[i].getSaldo()))
            
            self.__listClientes[i].setSaldo(nuevoSaldo)
            print("Saldo Actualizado:", self.__listClientes[i].getSaldo())
            
      
    def movimientosDelCliente(self,dni,gmovimientos):
        
        i = 0
        
        
        while i < len(self.__listClientes):
            
            if self.__listClientes[i].getDni() == dni:
            
                print("Cliente: {} {}".format(self.__listClientes[i].getNombre(),self.__listClientes[i].getApellido()))
                
                if float(self.__listClientes[i].getSaldo()) == gmovimientos.buscarMovimientos(self.__listClientes[i].getNroCuenta(),float(self.__listClientes[i].getSaldo())):
                    #Reutilizo el metodo 'bucarMovimientos() donde le envia el nro cuenta y saldo) donde
                    #retorna el saldo cambiado por movimientos y si el Saldo vuelve sin ningun cambio significa que no hubo movimientos
                    print("No Realizo movimientos en Abril del 2024")
                    break
           
            i = i+1
    def __lt__(self, otro_punto):
        
        # Sobrecargar el metodo '<'
        puntos_gestor_actual = self.__listClientes[0].getNroCuenta()
        puntos_otro_gestor = otro_punto.__listClientes[0].getNroCuenta()
        return puntos_gestor_actual > puntos_otro_gestor
    
    def ordenarListaClientes(self):
        
        self.__listClientes.sort(key=lambda cliente: cliente.getNroCuenta())
