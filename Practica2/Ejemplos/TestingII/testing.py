# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:16:07 2024

@author: Emmanuel
"""

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
    unittest.main()
