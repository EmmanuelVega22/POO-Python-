# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseActaNacimiento import ActaNacimiento

class RegistroCivil:
    
    __denominacion: str
    __domicilio: str
    __actas: list
    # Variables de clase
    __actaActual = 100
    __libroActual = 5
    
    def __init__(self, denominacion, domicilio):
    
        self.__denominacion = denominacion
        self.__domicilio = domicilio
        self.__actas=[]
        # Métodos de clase
        
    @classmethod
        
    def getActaActual(cls):
        
        cls.__actaActual+=1
        return cls.__actaActual
        
    @classmethod
    def getLibroActual(cls):
        
        return cls.__libroActual

    def inscribirPersona(self, persona, fecha):
        
        numeroActa = self.getActaActual()
        libro = self.getLibroActual()
        acta = ActaNacimiento(numeroActa, libro, fecha, persona, self)
        self.__actas.append(acta)

    def mostrarActas(self):
        
        for acta in self.__actas:
            print(acta)