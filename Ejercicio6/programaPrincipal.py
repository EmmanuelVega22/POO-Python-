# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import funciones
from gestorcuentas import GestorCuentas
from gestorTransacciones import GestorTransacciones

if __name__=='__main__':
    
    gcuentas = GestorCuentas()
    gtransacciones = GestorTransacciones()
    gcuentas.cargarCuentas()
    gtransacciones.cargarTransacciones()
    
    gcuentas.mostrar()
    print("__________________________")
    gtransacciones.mostrar()
    
    op = 0
    while op != '6':
        
        op = funciones.menu()
        
        if op == '1': 
            dni = input("Ingrese DNI del Cliente: ")
            
            gcuentas.listadoDatosCliente(dni,gtransacciones)
            
        elif op == '2':
                
            gcuentas.ModificarPorcentajeAnual()
            
        elif op == '3':
            gcuentas.mostrar()
            print("____________________________________________")
            print("Nuevo Saldos Actualizados")
            gcuentas.ActualizarSaldos()
            
        elif op == '4':
            
            cvu = input("Ingrese CVU del Cliente: ")
            
            gcuentas.InformarNuevoSaldo(gtransacciones,cvu)
            
        elif op == '5':
            
            gcuentas.ActualizarDatosEnUnArchivo()