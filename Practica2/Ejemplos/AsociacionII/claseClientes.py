# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Clientes:
    
    __idCliente: int
    __nombreyApellido: str
    __direccion: str
    __facturas: list

    def __init__(self,idCliente, nombreyApellido, direccion):
        
        self.__idCliente=idCliente
        self.__nombreyApellido=nombreyApellido
        self.__direccion=direccion
        self.__facturas = []
    def setFactura(self, unaFactura):
        
        self.__facturas.append(unaFactura)

    def getIdCliente(self):
        
        return self.__idCliente
    
    def getNyA(self):
        
        return self.__nombreyApellido
    
    def obtenerCuponDescuento(self):

        descuento = 0.0
        total = 0.0
        if len(self.__facturas)>2:
            for factura in self.__facturas:
                total+=factura.getTotal()
                descuento = total * 12/100
        
        return descuento
    
    def informe(self):
        
        total = 0.0
        print('Cliente: ',self.getNyA())
        for factura in self.__facturas:
            print('Factura {}, importe, {}'.format(factura.getNumeroFactura(), factura.getTotal()))
            total+=factura.getTotal()
            print('Total acumulado {0:8.2f}'.format(total))

    def verificarCuponDescuento(self):
        
        descuento=self.obtenerCuponDescuento()
        print('Cliente: {}, descuento: {}'.format(self.getNyA(),descuento))