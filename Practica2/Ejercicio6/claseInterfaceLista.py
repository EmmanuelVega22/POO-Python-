# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from abc import ABC, abstractmethod


class InterfaceLista(ABC):
    
    @abstractmethod
    def insertarCalefactor(self, calefactor, posicion):
        """Inserta un objeto en una posición determinada en la colección."""
        pass

    @abstractmethod
    def agregarCalefactor(self, calefactor):
        """Agrega un elemento al final de la colección."""
        pass

    @abstractmethod
    def mostrarCalefactor(self, posicion):
        """Muestra los datos del elemento almacenado en la posición especificada."""
        pass
