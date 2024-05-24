# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

import csv
from claseEdificio import Edificio

class GestorEdificios:
    
    __listEdificios : list
    
    def __init__(self):
        
        self.__listEdificios = []
    
    
    def agregarEdificios(self,nuevoEdificio):
        
        self.__listEdificios.append(nuevoEdificio)
    
    def cargarEdificios(self):
        
        archivoEdificio = open('EdificioNorte.csv')
        readerEdificio = csv.reader(archivoEdificio, delimiter = ';')
        
        nuevoEdificio = None
        
        for fila in readerEdificio:
            
            if len(fila)== 7:
                
                nuevoEdificio = Edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))            
                self.agregarEdificios(nuevoEdificio)

            else:
                                
                id_dep = int(fila[1])
                nom = fila[2]
                piso = int(fila[3])
                departamento = int(fila[4])
                dormitorio = int(fila[5])
                baño = int(fila[6])
                superficie = float(fila[7])
                nuevoEdificio.agregarDepartamento(id_dep,nom,piso,departamento,dormitorio,baño,superficie)
        
        
        archivoEdificio.close()
      
    def mostrar(self):
        
        for i in range(len(self.__listEdificios)):
            
            print(self.__listEdificios[i])
            print("_______________________________________________")
            print("_______________________________________________")
            
            #print(self.__listEdificios[0].getDepartamentos())
            
    def __del__(self):
        
        print('Borrando....')
        
    def buscarPropietarios(self,nom_edificio):
        
        i = 0
        
        while i < len(self.__listEdificios) and self.__listEdificios[i].getNombre() != nom_edificio:
            
            i = i+1
        
        if self.__listEdificios[i].getNombre() == nom_edificio:
            
            print("Edificio: ", self.__listEdificios[i].getNombre())
            self.__listEdificios[i].mostrarDepartamentos()
        
        else:
            print("No se encontró el edificio con el nombre especificado:", nom_edificio)
            
            
    def mostrarSuperficieTotalCubierta(self):
        
        for i in range(len(self.__listEdificios)):
            
            print("Edificio: ",self.__listEdificios[i].getNombre())
            
            print("Superficie Total Cubierta: ", self.__listEdificios[i].calcularSuperficieTotalCubierta())
    
    def SuperficieTotalCubiertaDeUnPropietario(self,nom_propietario):
        
        sup_cub = 0
        for i in range(len(self.__listEdificios)):
            
            sup_cub += self.__listEdificios[i].buscarSuperficieCubiertaDelPropietario(nom_propietario)
        
        
        print("Superficie Total Cubierta del Departamento: ", sup_cub)
        total = (sup_cub*100)/self.__listEdificios[i].calcularSuperficieTotalCubierta()
        print("Porcentaje del Total del Edificio: %.2f" % total)
        
    
    def mostrarPisos(self,num_piso):
        
        total = 0
        
        for i in range(len(self.__listEdificios)):
            
            total += self.__listEdificios[i].buscarPisos(num_piso)
        
        if total != 0:
            
            print("Numero de Piso {} la cantidad de Departamentos que tienen 3 dormitorios y mas de 1 baño son en total {}".format(num_piso,total))
            
        else:
            
            print("Ningun Departamento Cumple con esas Condiciones")