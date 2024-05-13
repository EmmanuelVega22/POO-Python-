# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Material:
    
    __material: str
    __caracteristicas:str
    __cant_Utilizado : int
    __costo_Adicional: float
    
    def __init__(self,material,caracteristicas,cant_util,costo_adic):
        
        self.__material = material
        self.__caracteristicas = caracteristicas
        self.__cant_Utilizado = cant_util
        self.__costo_Adicional = costo_adic
    
    def __str__(self):
        
        cadena = 'Material Refractario.\n'
        cadena +='Material: {}\n'.format(self.__material)
        cadena +='Caracteristicas: {}\n'.format(self.__caracteristicas)
        cadena +='Cant Utilizado: {}\tCosto Adicional: {}\n'.format(self.__cant_Utilizado,self.__costo_Adicional)
        
        return cadena
    
    def getMaterial(self):
        
        return self.__material
    
    def getCaracteristicas(self):
        
        return self.__caracteristicas
    
    def getCantUtilizado(self):
        
        return self.__cant_Utilizado
    
    def getCostoAdicional(self):
        
        return self.__costo_Adicional
    
        
        