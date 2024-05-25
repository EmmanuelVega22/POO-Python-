# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseComponenteNoticia import ComponentesNoticia

class Noticia:
    
    __fecha: str
    __autor: str
    __componentes = ComponentesNoticia
    
    def __init__(self,fecha,autor):
        
        self.__fecha = fecha
        self.__autor = autor
        
        self.__componentes = ComponentesNoticia('Titulo de la Noticia','Copete de la Noticia','Cuerpo de la Noticia')
    
    ''' O:
    def __init__(self,fecha,autor,componentes):
        
        self.__fecha = fecha
        self.__autor = autor
        
        self.__componentes = componentes
    
    '''
    def __del__(self):
        
        print("Borrando Componente de Noticias")
        del self.__componentes

   
    def __str__(self):
        
        cadena = 'Noticia:\n'
        cadena += 'Fecha: '+self.__fecha+'\n'
        cadena += 'Autor: '+self.__autor+'\n'
        cadena += str(self.__componentes)+'\n'
        
        return cadena
    
    def getFecha(self):
        
        return self.__fecha
    
    def getAutor(self):
        
        return self.__autor
    
    def mostrar(self):
        
        print(self)