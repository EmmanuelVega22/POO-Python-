# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseLibroImpreso import LibroImpreso
from claseCD import CD

class ColeccionLista:
    
    __publicaciones_editorial: list
    
    
    def __init__(self):
        
        self.__publicaciones_editorial = []
        
    
    def agregarPublicaciones(self,nuevaPublicacion):
        
        self.__publicaciones_editorial.append(nuevaPublicacion)
        
    
    def cargarColeccionLista(self):
        
        try:
            
            titulo = input("Ingrese Titulo de la Publicacion: ")
            categoria = input("Ingrese Categoria de la Publicacion: ")
            precio_base = float(input("Ingrse Precio Base de la Publicacion: "))
            
            tipo = input("¿Es un libro Impreso o un CD? (L/C)").upper()
            
            
            if tipo == 'L':
                
                autor = input("Ingrese Nombre del Autor: ")
                fecha = input("Ingrese la fecha de edicion (anio): ")
                paginas = int(input("Ingrese la cantidad de paginas: "))
                
                publicaciones = LibroImpreso(titulo,categoria,precio_base,autor,fecha,paginas)
            
            elif tipo == 'C':
                    
                tiempo_reprod= int(input("Ingrese tiempo de reproduccion en minutos: "))
                narrador = input("Ingrese el Narrador: ")
                
                publicaciones = CD(titulo,categoria,precio_base,tiempo_reprod,narrador)
            
            else:
                raise ValueError("Opcion no valida!")
                
            
            self.agregarPublicaciones(publicaciones)
            
            print("Publicaciones agregada con exito!")
            
        except (ValueError,TypeError) as e:
            
            print("Error:", e)
        
    def mostrar_tipo_publicacion(self,posicion):
        
        if 0 <= posicion < len(self.__publicaciones_editorial):
                        
            if isinstance(self.__publicaciones_editorial[posicion],LibroImpreso):
                
                print("La Publicacion en la posicion {} es un Libro Impreso.".format(posicion))
            
            elif isinstance(self.__publicaciones_editorial[posicion],CD):
                
                print("La Publicacion en la posicion {} es un CD".format(posicion))
                
        else:
            
            print("La posicion ingresada esta fuera de rango!")
    
    def mostrar_cantidad_publicaciones(self):
        
        cant_libros = 0
        cant_cd = 0
        for publicacion in self.__publicaciones_editorial:
            
            if isinstance(publicacion,LibroImpreso):
                
                cant_libros +=1
            
            elif isinstance(publicacion,CD):
                
                cant_cd +=1
        
        print("Cantidad de Libros Impresos: ",cant_libros)
        print("Cantidad de CDs", cant_cd)
    
    
    def mostrar_publicaciones(self):
        
        for publicacion in self.__publicaciones_editorial:
            
            print("Titulo: ", publicacion.getTitulo())
            print("Categoria: ", publicacion.getCategoria())
            print("Importe Venta: ", publicacion.importeDeVenta())
            