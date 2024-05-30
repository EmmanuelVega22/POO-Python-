# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseFactura import Factura
from claseClientes import Clientes
if __name__=='__main__':

    unCliente = Clientes(123, 'Luis Ventura', 'Mitre 156 (O)')
    factura1 = Factura('223','27/01/2020',4500, '30-33333323-1', 'Calzados la Zapa')
    unCliente.setFactura(factura1)
    factura2 = Factura('441','27/01/2020',6500, '27-12334333-1', 'Deportes ABC')
    unCliente.setFactura(factura2)
    factura3 = Factura('223','27/01/2020',8500, '20-31333333-1', 'Bicicletería la BICI')
    unCliente.setFactura(factura3)
    unCliente.informe()
    unCliente.verificarCuponDescuento() 