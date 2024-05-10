# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import csv

from Pedidos import Pedido
class GestorPedidos:
    
    __listPedidos : list
    
    
    def __init__(self):
        
        self.__listPedidos = []
    
    def __lt__(self, otro_gestor):
        # Comparar las patentes de los primeros pedidos de cada gestor
        # Obtener la patente del primer pedido del gestor actual
        patente_gestor_actual = self.__listPedidos[0].getPatente()
        # Obtener la patente del primer pedido del otro gestor
        patente_otro_gestor = otro_gestor.__listPedidos[0].getPatente()
        # Comparar las patentes y devolver el resultado
        return patente_gestor_actual < patente_otro_gestor
    
    def agregarPedido(self,nuevoPedido):
        
        self.__listPedidos.append(nuevoPedido)
    
    def cargarArchivoPedidos(self):
        
        archiPedidos = open('datosPedidos.csv')
        readerPedidos = csv.reader(archiPedidos,delimiter=',')
        
        
        for fila in readerPedidos:
            
            patente = fila[0]
            idPedido = fila[1]
            comidaPedida = fila[2]
            tiempoEst = fila[3]
            tiempoRealEnt = fila[4]
            precio = fila[5]
            
            nuevoPedido = Pedido(patente,idPedido,comidaPedida,tiempoEst,tiempoRealEnt,precio)
            self.agregarPedido(nuevoPedido)
        
        archiPedidos.close()
    
    def ordenarListPedidos(self):
        
        self.__listPedidos.sort(key=lambda pedido: pedido.getPatenteMoto())
        #permite especificar una función de clave de ordenamiento personalizada 
        #que se utilizará para determinar el orden de los elementos en la lista.        
        
        #Ejemplo:
        # Ordenar la lista por la longitud de las palabras
        #palabras.sort(key=lambda x: len(x))
    def mostrar(self):
        
        for i in range(len(self.__listPedidos)):
            
            print(self.__listPedidos[i])
            
    def cargarNuevosPedidos(self,patente):
        
            
            idPedido = input("Ingrese Id del Pedido: ")
            comidaPedida = input("Ingrese Comida Pedida: ")
            tiempoEst = int(input("Ingrese Tiempo Estimado de Entrega: "))
            tiempoRealEnt = int(input("Ingrese Tiempo Real Estimado de Entrega: "))
            precio = float(input("Ingrese Precio: "))
            nuevoPedido = Pedido(patente,idPedido,comidaPedida,tiempoEst,tiempoRealEnt,precio)
            
            self.agregarPedido(nuevoPedido)
    
    def modificarPedido(self):
        
        patente = input("Ingrese Patente: ")
        idPedido = input("Ingrese Id Pedido: ")
        
        i = 0
        
        while i<len(self.__listPedidos):
            
            if self.__listPedidos[i].getidPedido()== idPedido and self.__listPedidos[i].getPatenteMoto() == patente:
            
                break
            
            i= i+1
            
        if self.__listPedidos[i].getidPedido() == idPedido and self.__listPedidos[i].getPatenteMoto() == patente:
            
            tiempoRealEnt = input("Ingrese Tiempo Real de Entrega: ")
            
            self.__listPedidos[i].setTiempoRealEntrega(tiempoRealEnt)
        
            print("Tiempo de Entrega Cambiado: ", self.__listPedidos[i].getTiempoRealEntrega())
        
        else:
            
            print("No existe un Pedido con esa ID!")
            
    
    def buscarPedidosPorPatente(self,patente):
        
        cant = 0
        total = 0
        i =0
        
        while i<len(self.__listPedidos): 
            
            if self.__listPedidos[i].getPatenteMoto() == patente:
            
                cant = cant + 1
                total = total + float(self.__listPedidos[i].getTiempoRealEntrega())
            
            i= i+1
        
        return total/cant
    
    def mostrarListadoPorPatente(self,patente):
        
        total = 0
        i = 0
        print("|ID de Pedido      TiempoEstimado      TiempoReal      Precio")
        print("|____________________________________________________________")
        while i<len(self.__listPedidos):
            
            if self.__listPedidos[i].getPatenteMoto() == patente:
                
                print("|{}      {}      {}      {}".format(self.__listPedidos[i].getidPedido(),self.__listPedidos[i].getTiempoEstimado(),self.__listPedidos[i].getTiempoRealEntrega(),self.__listPedidos[i].getPrecio()))
        
                total = total + float(self.__listPedidos[i].getPrecio())
            
            i = i+1
            
        print("|Total: ", total,"                                           ")
        print("|Comision: ", (total*20)/100,"                               ")
        print("|____________________________________________________________")