# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseEmpresaConstructora import EmpresaConstructora

class Casa(EmpresaConstructora):
    
    __mts_cuadrados: float
    
    
    def __init__(self,localidad,direccion,superficie,terreno):
        
        super().__init__(localidad,direccion,superficie)
        
        self.__mts_cuadrados = terreno
        
        
    def __str__(self):
        
        cadena = super().__str__()
        cadena += 'Tipo: Casa\n'
        cadena += 'Metros Cuadrados del Terreno: '+ str(self.__mts_cuadrados) + '\n'
        
        return cadena
    
    def getMtsCuadrados(self):
        
        return self.__mts_cuadrados
    
    
    def importeDeVenta(self):
        
        precioConstruccion = self.getMtsCuadrados() * 1.80 * 20000
        
        importeVenta = self.getSuperficieCubierta() * 15 * precioConstruccion
        
        return importeVenta
