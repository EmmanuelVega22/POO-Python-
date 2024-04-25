import csv
class GestorFechaFutbol:

    __listFechas = list

    def __init__(self):
        
        self.__listFechas = []

    
    def agregarFechas(self,nuevaFecha):

        self.__listFechas.append(nuevaFecha)

    
    def cargarLista(self):

        archivoFechas = open('fechasFutbol.csv')
        readerFechas = csv.reader(archivoFechas,delimiter=',')

        for fila in readerFechas:

            self.agregarFechas(fila)

        archivoFechas.close()

    
    def mostrar(self):

        for i in range(len(self.__listFechas)):

            print(self.__listFechas[i])
