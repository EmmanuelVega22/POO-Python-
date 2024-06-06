# -*- coding: utf-8 -*-
"""
@author: USUARIO
"""

from claseProductoRefrigerado import ProductoRefrigerado
from claseProductoCongelado import ProductoCongelado
from claseNodo import Nodo
import csv

class Lista:
    
    __cabeza : Nodo
    __actual : Nodo
    __indice : int
    __tope : int
    
    
    def __init__(self):
        
        self.__cabeza = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        if self.__indice == self.__tope:
            
            self.__actual = self.__cabeza
            self.__indice = 0
            raise StopIteration
        
        else:
            
            self.__indice +=1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
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
                
            nodo = Nodo(nuevoProducto)
            
            if self.__cabeza == None:
                
                self.__cabeza = nodo
                self.__actual = nodo
                self.__tope +=1
                
            else:
                
                aux = self.__cabeza
                
                while aux.getSiguiente() != None:
                    
                    aux = aux.getSiguiente()
                
                aux.setSiguiente(nodo)
                self.__actual = self.__cabeza
                self.__tope +=1
                
                
                
    
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
            
        
        nodo = Nodo(nuevoProducto)
        
        if self.__cabeza == None:
            
            self.__cabeza = nodo
            self.__actual = nodo
            self.__tope +=1
        
        else:
            
            aux = self.__cabeza
            
            while aux.getSiguiente() != None:
                
                aux = aux.getSiguiente()
            
            
            aux.setSiguiente(nodo)
            self.__actual = self.__cabeza
            self.__tope +=1
        
        
    def mostrarPorPosicion(self,posicion):
        
        indice = 0
        
        for _ in range(posicion):
        
            
            if indice == posicion:
                
                if isinstance(self.__lista[posicion], ProductoCongelado):
                    
                    print("En la posicion {} hay un objecto de tipo Congelado".format(posicion))
                
                elif isinstance(self.__lista[posicion], ProductoRefrigerado):
                    
                    print("En la posicion {} hay un objecto de tipo Refrigerado".format(posicion))
            else:
                
                indice +=1
    
    def cantidadDeTipoProductos(self):
        
        
        cantCongelados= 0
        cantRefrigerados=0
         
        aux = self.__cabeza
        
        while aux != None:
            
            if isinstance(aux.getDato(),ProductoCongelado):
                
                cantCongelados+=1
                
            elif isinstance(aux.getDato(),ProductoRefrigerado):
                
                cantRefrigerados+=1
            
            aux = aux.getSiguiente()
            
        print("La cantidad de Productos Congelados: ",cantCongelados)
        
        print("La cantidad de Productos Refrigerados:",cantRefrigerados)
        
    
    
    def mostrarProductos(self):
        
        aux = self.__cabeza
        
        while aux != None:
            
            
            print(aux.getDato())
            aux = aux.getSiguiente()
            
    
    def productos(self):
        
        aux = self.__cabeza
        
        while aux != None:
            
            print("Nombre Producto: ",aux.getDato().getNombreProducto() )
            print("Pais Origen: ", aux.getDato().getPaisOrigen())
            print("Temperatura Mantenida: ", aux.getDato().getTemperatura())
            print("Importe de Venta:", aux.getDato().importeDeVenta())
            
            aux = aux.getSiguiente()