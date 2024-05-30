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
	
    #calefactor.cargarCalefactores()
    #d = calefactor.toJSON()
    #jsonF.guardarJSONArchivo(d,'calefactores.json')    
    #calefactor.mostrarDatos()
    
    while op != '7':
        
        op = menu()
        
        if op=='1':
            calefactor.insertarCalefactor()	
            calefactor.mostrarDatos()

        elif op =='2':
            d=calefactor.toJSON()
            jsonF.guardarJSONArchivo(d,'calefactores.json')
        elif op =='3':
            diccionario=jsonF.leerJSONArchivo('calefactores.json')
            calefactor=jsonF.decodificarDiccionario(diccionario)
            calefactor.mostrarDatos()
        elif op == '4':
            pass
        elif op =='4':
            pass
        elif op == '5':
            pass
        elif op == '6':
            pass