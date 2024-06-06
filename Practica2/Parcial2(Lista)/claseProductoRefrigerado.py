# -*- coding: utf-8 -*-
"""
@author: USUARIO
"""
from datetime import datetime
from claseProducto import Productos

class ProductoRefrigerado(Productos):

    __codigo_organismo: str
    
    
    def __init__(self, nom_producto, fecha_envasado, fecha_vencimiento,
                 temperatura, pais, num_lote, costo,codigo_organismo):
        
        
        super().__init__(nom_producto, fecha_envasado, fecha_vencimiento,
                         temperatura, pais, num_lote, costo)
        
        self.__codigo_organismo = codigo_organismo
       
    
    def __str__(self):
        
        cadena = super().__str__()
        
        cadena += "Producto Refrigerado\n"
        cadena += str(self.__codigo_organismo) + '\n'
        
        return cadena
    
    def getCodigoOrganismo(self):
        
        return self.__codigo_organismo
    
    def importeDeVenta(self):
        
        mes_vencimiento = self.getFechaVencimiento().month - datetime.now().month
        
        if mes_vencimiento <= 2:
            
            return float(self.getCostoBase()) * 0.9#menos del 10% porciento
        
        else:
            
            return float(self.getCostoBase()) + (float(self.getCostoBase()) * 1.01)
        
        
    
    