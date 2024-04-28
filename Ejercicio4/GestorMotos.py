# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import csv

from Moto import Moto

class GestorMotos:
    
    __listMotos : list
    
    
    def __init__(self):
        
        self.__listMotos = []
        
   
    def agregarMotos(self,nuevaMotos):
        
        self.__listMotos.append(nuevaMotos)
        
    
    def cargarArchivoMotos(self):
        
        
        archiMotos = open('datosMotos.csv')
        readerMotos = csv.reader(archiMotos,delimiter=',')
        
        
        for fila in readerMotos:
            
            patente = fila[0]
            marca = fila[1]
            nombreC = fila[2]
            apellidoC = fila[3]
            kilometraje = fila[4]
            
            nuevaMoto =Moto(patente,marca,nombreC,apellidoC,kilometraje)
            self.agregarMotos(nuevaMoto)
        
        archiMotos.close()
    
    def mostrar(self):
        
        for i in range(len(self.__listMotos)):
            
            print(self.__listMotos[i])
            
    def buscarPatente(self,patente):
        
        i=0
        
        while i < len(self.__listMotos) and self.__listMotos[i].getpatente() != patente:
           
            i= i+1
        
        if self.__listMotos[i].getpatente() == patente:
            
            
            return self.__listMotos[i].getpatente()
        
        else:
            
            print("No existe una moto con esa Patente!")
            return False
    
    
    def mostrarDatosMoto(self,patente,total):
        
        i=0
        
        while i < len(self.__listMotos) and self.__listMotos[i].getpatente() != patente:
            
            i=i+1
        
        
        if self.__listMotos[i].getpatente() == patente:
            
            print("Patente:", patente)
            print("Nombre Conductor: ", self.__listMotos[i].getnombreC())
            print("Apellido Conductor: ", self.__listMotos[i].getapellidoC())
            print("Tiempo Promedio de Entrega: ", total)
        
    def listadoMotos(self,gestor):
        
        for i in range(len(self.__listMotos)):
            print(" ___________________________________________________________")
            print("|Patente de Moto: ", self.__listMotos[i].getpatente())
            print("|Conductor: {} {}".format(self.__listMotos[i].getnombreC(),self.__listMotos[i].getapellidoC()))
            print("|___________________________________________________________")
            gestor.mostrarListadoPorPatente(self.__listMotos[i].getpatente())
            