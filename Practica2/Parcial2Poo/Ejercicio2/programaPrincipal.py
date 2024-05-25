# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseLista import Lista
from menu import menu
import unittest
from claseDepartamento import Departamento
from claseCasa import Casa

class TestImporteDeVenta(unittest.TestCase):

    def test_importe_de_venta_departamento(self):
        
        print("Testing de Importe de Venta Departamento.....")
        departamento = Departamento("Albardon", "Albardon Sur 310", 100, 10, 3, 1, 101, 5)
        importe_venta_esperado = 100 * 15 * (3 * 17000)
        self.assertEqual(departamento.importeDeVenta(), importe_venta_esperado)
        #assertEqual: Aceptan dos objetos comparables, y tendra
        #éxito si los objetos son iguales
    def test_importe_de_venta_casa(self):
        
        print("Testing de Importe de Venta Casa.....")
        casa = Casa("9 Julio", "9 Julio Norte 742", 200, 300)
        importe_venta_esperado = 200 * 15 * (300 * 1.80 * 20000)
        self.assertEqual(casa.importeDeVenta(), importe_venta_esperado)
        #assertEqual: Aceptan dos objetos comparables, y tendra
        #éxito si los objetos son iguales



if __name__ == '__main__':
    
    
    clista = Lista()
    
    
    op = 0
    
    while op != '5':
        
        op = menu()
        
        if op == '1':
            
            clista.InsertarInmuebles()
            clista.mostrar()
            
        elif op == '2':
            
            dormitorios = int(input("Ingrese la Cantidad de Dormitorios: "))
            clista.mostrar_inmuebles_por_dormitorios(dormitorios)
        elif op == '3':
            
            clista.mostrar_inmuebles_tipo_casa()
            
        elif op == '4':
            
            unittest.main()
