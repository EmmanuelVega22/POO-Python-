# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseDepartamento import Departamento

class Edificio:
    
    __id_edificio: int
    __nombre_edificio : str
    __direccion: str
    __nombre_empresa: str
    __cant_pisos: int
    __cant_departamentos: int
    __departamentos: list
    
    def __init__(self,id_edificio,nombre,direccion,nombre_empresa,cant_pisos,cant_departamentos):
        
        self.__id_edificio = id_edificio
        self.__nombre_edificio = nombre
        self.__direccion = direccion
        self.__nombre_empresa = nombre_empresa
        self.__cant_pisos = cant_pisos
        self.__cant_departamentos = cant_departamentos
        self.__departamentos=[]
    
    def agregarDepartamento(self,id_departamento,nomYapell,num_piso,num_departamento,
                            cant_dormitorios,cant_baños,superficie):
        
        self.__departamentos.append(Departamento(id_departamento,nomYapell,num_piso,num_departamento,
                                           cant_dormitorios,cant_baños,superficie))
    
    def __str__(self):
        
        
        cadena ='Edificio:\n'
        cadena +='ID: {}\n'.format(self.__id_edificio)
        cadena +='Nombre del Edificio: {}\n'.format(self.__nombre_edificio)
        cadena +='Nombre de la Empresa: {}\n'.format(self.__nombre_empresa)
        cadena +='Direccion: {}\n'.format(self.__direccion)
        cadena +='Cant Pisos: {}\tCantDepartamentos: {}\n'.format(self.__cant_pisos,self.__cant_departamentos)
        cadena+='Departamentos:\n'
        for departamento in self.__departamentos:
            cadena += str(departamento) + '\n'
        return cadena
    
    def getNombre(self):
        
        return self.__nombre_edificio
    
    def __del__(self):
        
        print('Borrando....')
        del self.__departamentos
        
    def mostrarDepartamentos(self):
        
        for i in range(len(self.__departamentos)):
            
            print("Id Departamento: ",self.__departamentos[i].getIdDepartamento())
            print("Nombre y Apellido: ",self.__departamentos[i].getNombreyApellido())
            
     
    def calcularSuperficieTotalCubierta(self):
        
        total = 0
        
        for i in range(len(self.__departamentos)):
            
            total += self.__departamentos[i].getSuperficieCubierta()
        
        return total
    
    def buscarSuperficieCubiertaDelPropietario(self,nom_propietario):
        
        i=0
        total = 0
        while i < len(self.__departamentos):
            
            if self.__departamentos[i].getNombreyApellido() == nom_propietario:
                
                total += self.__departamentos[i].getSuperficieCubierta()
        
            i+=1
        return total
    
    def buscarPisos(self,num_piso):
        
        i = 0
        cont = 0
        while i < len(self.__departamentos):
            
            if self.__departamentos[i].getNumPiso() == num_piso:
                
                if self.__departamentos[i].getCantDormitorios() == 3 and self.__departamentos[i].getCantBaños() > 1:
                    cont+=1
            
            i+=1
        return cont