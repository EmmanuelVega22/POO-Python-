# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Departamento:
    
    __id_departamento: int
    __nombreYapellido: str
    __num_piso: int
    __num_departamento: int
    __cant_dormitorios: int
    __cant_baños: int
    __superficie_cubierta: float
    
    def __init__(self,id_departamento,nomYapell,num_piso,num_departamento,cant_dormitorios,
                 cant_baños,superficie):
        
        self.__id_departamento = id_departamento
        self.__nombreYapellido = nomYapell
        self.__num_piso = num_piso
        self.__num_departamento = num_departamento
        self.__cant_dormitorios = cant_dormitorios
        self.__cant_baños = cant_baños
        self.__superficie_cubierta = superficie
    
    def __str__(self):
            
        cadena ='Departamentos:\n'
        cadena +='ID: {} '.format(self.__id_departamento)
        cadena +='Nombre y Apellido: {}\n'.format(self.__nombreYapellido)
        cadena +='Numero Piso: {}\tNumero Departamento: {}\n'.format(self.__num_piso,self.__num_departamento)
        cadena +='CantDormitorios: {}\tCantBaños: {}\n'.format(self.__cant_dormitorios,self.__cant_baños)
        cadena +='Superficie Cubierta: {}\n'.format(self.__superficie_cubierta)
        return cadena
    
    
    def getIdDepartamento(self):
        
        return self.__id_departamento
    
    def getNombreyApellido(self):
        
        return self.__nombreYapellido
    
    def getNumPiso(self):
        
        return self.__num_piso
    
    def getNumDepartamento(self):
        
        return self.__num_departamento
    
    def getCantDormitorios(self):
        
        return self.__cant_dormitorios
    
    def getCantBaños(self):
        
        return self.__cant_baños
    
    def getSuperficieCubierta(self):
        
        return self.__superficie_cubierta
    
    
        