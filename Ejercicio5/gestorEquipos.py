import csv
from equipo import Equipo

class GestorEquipos:

    __listEquipos : list

    def __init__(self):
        
        self.__listEquipos = []

    
    def agregarEquipos(self,nuevoEquipo):

        self.__listEquipos.append(nuevoEquipo)

    def cargarLista(self):

        archivoEquipos = open('equipos2024.csv')
        readerEquipos = csv.reader(archivoEquipos,delimiter=',')


        for fila in readerEquipos:

            self.agregarEquipos(fila)
        
        archivoEquipos.close()

    
    def mostrar(self):

        for i in range(len(self.__listEquipos)):

            print(self.__listEquipos[i])

    def buscar(self,nombrequipo):

        i = 0

        while i< len(self.__listEquipos) and self.__listEquipos[i][1] != nombrequipo:

            i = i+1
        

        if self.__listEquipos[i][1] == nombrequipo:

            


