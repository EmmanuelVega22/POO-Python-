# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:57:31 2024

@author: Emmanuel
"""
from claseLista import Lista,ObjectEncoder
from menu import menu

if __name__=='__main__':
    
    jsonF=ObjectEncoder()
    calefactor = Lista()
    op =0
	#######################
    #Carga un Archivo JSON#
    #######################
    '''
    #calefactor.cargarCalefactores()
    #d = calefactor.toJSON()
    #jsonF.guardarJSONArchivo(d,'calefactores.json')    
    #calefactor.mostrarDatos()
    '''
    ###############################
    #Leer Datos de un Archivo JSON#
    ###############################
    
    diccionario=jsonF.leerJSONArchivo('calefactores.json')
    calefactor=jsonF.decodificarDiccionario(diccionario)
    for dato in calefactor:

        print(dato)    

    while op != '7':
        
        op = menu()
        
        if op=='1':
            calefactor.insertarCalefactor()	
            calefactor.mostrarDatos()

        elif op =='2':
            calefactor.agregarUnCalefactor()
        elif op =='3':
            posicion = int(input("Ingrese una posicion: "))
            calefactor.tipoDeDatoEnDichaPosicion(posicion)
        elif op == '4':
            calefactor.calefactorGasNaturalConMenoPrecio()
        elif op =='5':
            marca = input("Ingrese Marca de Calefactor Electrico: ")
            calefactor.mostrarMarcaCalefactorElectrico(marca)
        elif op == '6':
            pass
