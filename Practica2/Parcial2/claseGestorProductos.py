# -*- coding: utf-8 -*-
"""
@author: USUARIO
"""

from claseProductoRefrigerado import ProductoRefrigerado
from claseProductoCongelado import ProductoCongelado
import csv

class GestorProductos:
    
    __lista : list
    
    
    def __init__(self):
        
        self.__lista = []
        
    
    def agregarProducto(self,nuevoProducto):
        
        self.__lista.append(nuevoProducto)
    
    def cargarLista(self):
        
        archivo = open("Productos.csv")
        
        reader = csv.reader(archivo,delimiter=',')
        
        for fila in reader:
            
            tipo_producto = fila[0]
            
            if tipo_producto == 'C':
                
                nuevoProducto = ProductoCongelado(fila[1],fila[2],fila[3],fila[4],
                                                  fila[5],fila[6],fila[7],fila[8],
                                                  fila[9])
                
                #nuevoProducto = ProductoCongelado(*fila[1:])
            
            elif tipo_producto == 'R':
                
                nuevoProducto = ProductoRefrigerado(fila[1],fila[2],fila[3],fila[4],
                                                  fila[5],fila[6],fila[7],fila[8])
            
                #nuevoProducto = ProductoRefrigerado(*fila[1:])
                
            self.agregarProducto(nuevoProducto)
    
    def insertarProducto(self):
        
        nombre_prod = input("Ingrese Nombre Producto: ")
        fecha_envasado = input("Ingrese Fecha Envasado: ")
        fecha_vencimiento = input("Ingrese fecha de vencimiento: ")
        temperatura = input("Ingrese Temperatura: ")
        pais = input("Ingrese Pais de Origen: ")
        num_lote = int(input("Ingrese Numero de Lote: "))
        costo_base = float(input("Ingrese Costo Base: "))
        
        op = input("¿Es Producto Congelado o Refrigerado (C/R): ?").upper()
        
        if op == 'C':
            
            composicion_aire = input("Ingrese la Composicion de Aire: ")
            metodo_congelacion = input("Ingrese Metodo de Congelacion: ")
            
            nuevoProducto = ProductoCongelado(nombre_prod,fecha_envasado,fecha_vencimiento,temperatura, pais, num_lote, costo_base, composicion_aire, metodo_congelacion)
            
        
        elif op == 'R':
            
            codigo_organismo = input("Ingrese Codigo de Organismo: ")
            
            nuevoProducto = ProductoRefrigerado(nombre_prod, fecha_envasado, fecha_vencimiento, temperatura, pais, num_lote, costo_base, codigo_organismo)
            
        
        self.agregarProducto(nuevoProducto)
        
        
        
    def mostrarPorPosicion(self,posicion):
        
        
        if isinstance(self.__lista[posicion], ProductoCongelado):
                
            print("En la posicion {} hay un objecto de tipo Congelado".format(posicion))
            
        elif isinstance(self.__lista[posicion], ProductoRefrigerado):
                
            print("En la posicion {} hay un objecto de tipo Refrigerado".format(posicion))
        
    
    def cantidadDeTipoProductos(self):
        
        
        cantCongelados= 0
        cantRefrigerados=0
        
        for fila in self.__lista:
            
            if isinstance(fila,ProductoCongelado):
                
                cantCongelados+=1
                
            elif isinstance(fila,ProductoRefrigerado):
                
                cantRefrigerados+=1
            
            
        print("La cantidad de Productos Congelados: ",cantCongelados)
        
        print("La cantidad de Productos Refrigerados:",cantRefrigerados)
        
    
    
    def mostrarProductos(self):
        
        for producto in self.__lista:
            
            print(producto)
            
    
    def productos(self):
        
        
        for i in range(len(self.__lista)):
            
            print("Nombre Producto: ", self.__lista[i].getNombreProducto() )
            print("Pais Origen: ", self.__lista[i].getPaisOrigen())
            print("Temperatura Mantenida: ", self.__lista[i].getTemperatura())
            print("Importe de Venta:", self.__lista[i].importeDeVenta())
            