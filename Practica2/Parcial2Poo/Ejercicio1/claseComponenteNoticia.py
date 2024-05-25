# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class ComponentesNoticia:
    
    __titulo: str
    __copete: str
    __cuerpo: str
    
    
    def __init__(self,titulo,copete,cuerpo):
        
        self.__titulo = titulo
        self.__copete = copete
        self.__cuerpo = cuerpo
    
    def __str__(self):
        
        cadena = 'Componentes:\n'
        cadena += 'Titulo: '+ self.__titulo + '\n'
        cadena += 'Copete: '+ self.__copete + '\n'
        cadena += 'Cuerpo: '+ self.__cuerpo + '\n'
        
        return cadena
    
    def getTitulo(self):
        
        return self.__titulo
    
    def getCopete(self):
        
        return self.__copete
    
    def getCuerpo(self):
        
        return self.__cuerpo
        
        