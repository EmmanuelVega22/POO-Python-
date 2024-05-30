# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseCuentaCampus import CuentaCampus
class Profesor:
    __dni: int
    __apellido: str
    __nombre: str
    __cuentaCampus: object
    
    def __init__(self, dni, apellido, nombre):

        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        idCuenta=CuentaCampus.getIdCuenta()
        dominio=CuentaCampus.getDominio()
        usuario=nombre.lower()+apellido.lower()+dominio
        self.__cuentaCampus=CuentaCampus(idCuenta,usuario,dni)

    def __del__(self):
        
        print('Borrando cuenta de usuario....')
        del self.__cuentaCampus
    
    def __str__(self):

        cadena ='Profesor: \n'
        cadena += 'Apellido y nombre: {}, {}\n'.format(self.__apellido, self.__nombre)
        cadena+=str(self.__cuentaCampus)
        return cadena

    def mostrar(self):

    	print(self)