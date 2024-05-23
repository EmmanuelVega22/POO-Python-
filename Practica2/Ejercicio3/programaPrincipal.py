# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from menu import menu
from gestorMatricula import GestorMatriculas
from gestorEmpleados import GestorEmpleados
from gestorProgramaCapacitacion import GestorProgramaCapacitacion

if __name__=='__main__':
    
    gempleado = GestorEmpleados()
    gprograma = GestorProgramaCapacitacion()
    gmatricula = GestorMatriculas()
    
    gempleado.cargarEmpleados(gprograma)
    gprograma.cargarProgramasCapacitacion()
    
    
    gempleado.registrarEmpleado_Programa(gprograma,gmatricula)
    
    gempleado.mostrar()
    print("________________________")
    print("________________________")
    
    gprograma.mostrar()
    print("________________________")
    print("________________________")
    
    gmatricula.mostrar()
    print("________________________")
    print("________________________")
    
    op = 0
    
    while(op != '4'):
        
        op = menu()
        
        if op == '1':
            
            id_empleado = int(input("Ingrese ID de un empleado: "))
            gmatricula.buscarEmpleado(id_empleado)
        
        elif op == '2':
            nom_capacitacion = input("Ingrse Nombre de la Capacitacion: ")
            gmatricula.buscarCapacitacion(nom_capacitacion)
            
        elif op == '3':
            
            gempleado.buscarEmpleadosConMatriculacion()