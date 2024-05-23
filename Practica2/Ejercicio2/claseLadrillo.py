# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Ladrillo:
    
    __alto = 7
    __largo = 25
    __ancho = 15
    __cantidad : int
    __identificador : int
    __kgMatprimUtil:float
    __costo: float
    __material:object
    
    
    @classmethod
    def getAlto(cls):
        
        return cls.__alto
    
    @classmethod
    def getLargo(cls):
        
        return cls.__largo
    
    @classmethod
    def getAncho(cls):
        
        return cls.__ancho
    
    def getCantidad(self):
        
        return self.__cantidad
    
    def getIdentificador(self):
        
        return self.__identificador
    
    def getKgMateriales(self):
        
        return self.__kgMatprimUtil
    
    def getCosto(self):
        
        return self.__costo
    
    def getMaterial(self):
        
        return self.__material
    def __init__(self,cantidad,identificador,kgmat,costo,material):
        
        self.__alto = self.getAlto()
        self.__largo = self.getLargo()
        self.__ancho = self.getAncho()
        self.__cantidad = cantidad
        self.__identificador = identificador
        self.__kgMatprimUtil = kgmat
        self.__costo = costo
        self.__material = material
        #self.__material.append(material)
     
    def __str__(self):
        
        cadena = 'Ladrillo.\n'
        cadena +='Identificador: {}\n'.format(self.__identificador)
        cadena +='Alto:{} \tLargo:{} \tAncho:{}\n'.format(self.getAlto(),self.getLargo(),self.getAncho())
        cadena +='Cantidad: {}\n'.format(self.__cantidad)
        cadena +='MateriaPrima Utilizado: {}kg\tCosto: {}\n'.format(self.__kgMatprimUtil,self.__costo)
        cadena += str(self.__material)
        '''
        for materiales in self.__material:
            cadena += str(materiales) + '\n'
        return cadena
        '''
      
    def costoDeFabricacion(self):
        
        return self.__material.getCostoAdicional()+self.getCosto()
    
    def caracteristicaDelLadrillo(self):
        
        return self.__material.getCaracteristicas()
    
    def materialDelLadrillo(self):
        
        return self.__material.getMaterial()