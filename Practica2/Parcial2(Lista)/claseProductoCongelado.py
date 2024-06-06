# -*- coding: utf-8 -*-
"""
@author: USUARIO
"""

from claseProducto import Productos

class ProductoCongelado(Productos):
    
    __composicion_aire:str
    __metodo_congelacion:str
    
    
    def __init__(self, nom_producto, fecha_envasado, fecha_vencimiento,
                 temperatura, pais, num_lote, costo,composicion_aire,
                 metodo_congelacion):
        
        super().__init__(nom_producto, fecha_envasado, fecha_vencimiento,
                         temperatura, pais, num_lote, costo)
    
        
        self.__composicion_aire = composicion_aire
        self.__metodo_congelacion = metodo_congelacion
        
    
    def __str__(self):
        
        cadena = super().__str__()
        
        cadena += "Producto Congelado:\n"
        cadena += self.__composicion_aire + '\n'
        cadena += self.__metodo_congelacion + '\n'
        
        return cadena
    
    def getComposicionAire(self):
        
        return self.__composicion_aire
    
    def getMetodoCongelacion(self):
        
        return self.__metodo_congelacion
    
    
    def importeDeVenta(self):
        
        if self.getMetodoCongelacion() == 'Mecanico':
            
            return float(self.getCostoBase()) + (float(self.getCostoBase()) * 1.15)
        
        elif self.getMetodoCongelacion() == 'Criogenico':
            
            return float(self.getCostoBase()) + (float(self.getCostoBase()) * 1.15)
        
        