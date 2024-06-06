# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseNodo import Nodo
from claseInterfaceLista import InterfaceLista
import json
from pathlib import Path


class Lista(InterfaceLista):

    __cabeza = Nodo
    
    
    def __init__(self):
        
        self.__cabeza = None
        
    
    def insertarCalefactor(self, calefactor, posicion): 
        pass
    
    def agregarCalefactor(self, calefactor):
        pass
    
    def mostrarCalefactor(self, posicion):
        pass
    
    
    def toJSON(self):
        
        d = dict(
                __class__=self.__class__.__name__,
                calefactores=[calefactor.toJSON() for calefactor in self.__cabeza]
                )
        return d
    
    
