# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import json
from pathlib import Path


class ObjectEncoder(object):
      
    def decodificarDiccionario(self,d):
            
        if '__class__' not in d:
            return d
            
        else:

            class_name=d['__class__']
            class_= eval(class_name)

            if class_name == 'Lista':

                print("Dentro del decodificador y dentor del if class_name==lista")   
                puntos=d['calefactores']
                dPunto = puntos[0]
                manejador = class_()
                print(dPunto)
                for i in range(len(puntos)):

                    print("El tamano del archivo es: ",len(puntos))
                    print("Dentro del for con i=",i)      
                    dPunto = puntos[i]
                    class_name = dPunto.pop('__class__')
                    class_=eval(class_name)
                    atributos = dPunto['__atributos__']
                    unPunto = class_(**atributos)
                    print(unPunto)
                    manejador.agregarCalefactor(unPunto)

        return manejador
    
    def guardarJSONArchivo(self,diccionario,archivo):
        
        with Path(archivo).open("w",encoding="UTF-8") as destino:
    
            json.dump(diccionario,destino,indent=4)
            destino.close()
	
    def leerJSONArchivo(self,archivo):
        
        with Path(archivo).open(encoding="UTF-8") as fuente:
            
            diccionario = json.load(fuente)
            fuente.close()
        
        return diccionario

from claseNodo import Nodo
from claseCalefactorElectrico import CalefactorElectrico
from claseCalefactorGasNatural import CalefactorGasNatural
from claseInterfazLista import InterfazLista

class Lista(InterfazLista):
    
    __cabeza = Nodo
    
    def __init__(self):
        
        self.__cabeza = None
        
    def mostrarDatos(self):
        
        aux = self.__cabeza
        
        while aux != None:
            
            print(aux.getDato())
            
            aux = aux.getSiguiente()
    
    def toJSON(self):

        d = dict(
            __class__=self.__class__.__name__,
            calefactores=None
        )
        
        aux = self.__cabeza
        while aux is not None:
            if d["calefactores"] is None:
                d["calefactores"] = []
            d["calefactores"].append(aux.getDato().toJSON())
            aux = aux.getSiguiente()
        return d
    
    def agregarCalefactor(self,calefactor):
    
        nodo = Nodo(calefactor)
        
        print("entro al agregar calefactor: ",self.__cabeza)
        
        if self.__cabeza == None:
            
            self.__cabeza = nodo
            print(self.__cabeza.getDato())
        
        else:

            aux = self.__cabeza
            while aux.getSiguiente() != None:
            
                aux = aux.getSiguiente()
            
            aux.setSiguiente(nodo)
    
    def cargarCalefactores(self):
        
        op = 'si'
        
        while op != 'NO':
            
            if self.__cabeza == None:
                
                marca = input("Ingrese Marca: ")
                modelo = input("Ingrese Modelo: ")
                pais = input("Ingrese Pais de Fabricacion: ")
                precio = float(input("Ingrese Precio: "))
                forma_pago = input("Ingrese Forma de Pago: ")
                cuotas = int(input("Ingrese Cantidad de Cuotas('1' si es de contado): "))
                
                tipo = input("¿Es un Calefactor Electrico o a Gas Natural? (E/G): ").upper()
                
                if tipo == 'E':
                    
                    potencia = input("Ingrese Potencia Maxima: ")
                    
                    calefactor = CalefactorElectrico(marca,modelo,pais,precio,forma_pago,cuotas,potencia)
                
                elif tipo == 'G':
                    
                    matricula = input("Ingrese Matricula: ")
                    calorias = input("Ingrese Calorias: ")
                    
                    calefactor = CalefactorGasNatural(marca,modelo,pais,precio,forma_pago,cuotas,matricula,calorias)
                
                
                nodo = Nodo(calefactor)
                self.__cabeza = nodo
            
            
            else:
                
                aux = self.__cabeza
                
                while aux.getSiguiente() != None:
                    
                    aux = aux.getSiguiente()
                
                marca = input("Ingrese Marca: ")
                modelo = input("Ingrese Modelo: ")
                pais = input("Ingrese Pais de Fabricacion: ")
                precio = float(input("Ingrese Precio: "))
                forma_pago = input("Ingrese Forma de Pago: ")
                cuotas = int(input("Ingrese Cantidad de Cuotas('1' si es de contado): "))
                
                tipo = input("¿Es un Calefactor Electrico o a Gas Natural? (E/G): ").upper()
                
                if tipo == 'E':
                    
                    potencia = input("Ingrese Potencia Maxima: ")
                    
                    calefactor = CalefactorElectrico(marca,modelo,pais,precio,forma_pago,cuotas,potencia)
                
                elif tipo == 'G':
                    
                    matricula = input("Ingrese Matricula: ")
                    calorias = input("Ingrese Calorias: ")
                    
                    calefactor = CalefactorGasNatural(marca,modelo,pais,precio,forma_pago,cuotas,matricula,calorias)
                                
                nodo = Nodo(calefactor)
                
                aux.setSiguiente(nodo)
            
            op = input("¿Cargar otro calefactor? (Si/No): ").upper()

    
    def insertarCalefactor(self):
        
        marca = input("Ingrese Marca: ")
        modelo = input("Ingrese Modelo: ")
        pais = input("Ingrese Pais de Fabricacion: ")
        precio = float(input("Ingrese Precio: "))
        forma_pago = input("Ingrese Forma de Pago: ")
        cuotas = int(input("Ingrese Cantidad de Cuotas('1' si es de contado): "))
        
        tipo = input("¿Es un Calefactor Electrico o a Gas Natural? (E/G): ").upper()
                
        if tipo == 'E':
                    
            potencia = input("Ingrese Potencia Maxima: ")
                
            calefactor = CalefactorElectrico(marca,modelo,pais,precio,forma_pago,cuotas,potencia)
                
        elif tipo == 'G':
                    
            matricula = input("Ingrese Matricula: ")
            calorias = input("Ingrese Calorias: ")
                    
            calefactor = CalefactorGasNatural(marca,modelo,pais,precio,forma_pago,cuotas,matricula,calorias)
                
                
        nodo = Nodo(calefactor)
        
        posicion = int(input("Ingrese la posicion que desea insertar: "))

        if posicion == 1:
            
            nodo.setSiguiente(self.__cabeza)
            self.__cabeza =nodo
        
        else:
             
            aux = self.__cabeza
            print("Insertar Calefactor aux=",aux.getDato())
            anterior = None
            for _ in range(posicion-1):
                
                if aux == None:
                    
                    raise IndexError("La posición excede el tamaño de la colección")
                
                else:
                    
                    anterior = aux
                    aux = aux.getSiguiente()
            
            if aux != None:
                
                anterior.setSiguiente(nodo)
                nodo.setSiguiente(aux)                            