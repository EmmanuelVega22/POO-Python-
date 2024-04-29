import csv
import msvcrt
from fechaFutbol import FechaFutbol
class GestorFechaFutbol:

    __listFechas = list

    def __init__(self):
        
        self.__listFechas = []

    def __del__(self): #Destructor
    
        print("Se va destruir el Gestor Fechas!")
        
    def agregarFechas(self,nuevaFecha):

        self.__listFechas.append(nuevaFecha)

    
    def cargarListaFechas(self):

        archivoFechas = open('datosFechas.csv')
        readerFechas = csv.reader(archivoFechas,delimiter=',')

        for fila in readerFechas:
            
            fechaPartido = fila[0]
            idEquipoLocal = fila[1]
            idEquipoVisitante = fila[2]
            cantGolesLocal = fila[3]
            cantGolesVisitante = fila[4]
            
            nuevaFecha = FechaFutbol(fechaPartido,idEquipoLocal,idEquipoVisitante,cantGolesLocal,cantGolesVisitante)
            self.agregarFechas(nuevaFecha)

        archivoFechas.close()

    
    def mostrar(self):

        for i in range(len(self.__listFechas)):

            print(self.__listFechas[i])
     
    def __lt__(self, otro_punto):
        # Sobrecargar el metodo '<'
        primer_punto = (self.x ** 2 + self.y ** 2) ** 0.5
        segundo_punto = (otro_punto.x ** 2 + otro_punto.y ** 2) ** 0.5
        return primer_punto < segundo_punto
    
    def __gt__(self, otro_punto):
        # Sobrecargar el metodo '>'
        primer_punto = (self.x ** 2 + self.y ** 2) ** 0.5
        segundo_punto = (otro_punto.x ** 2 + otro_punto.y ** 2) ** 0.5
        return primer_punto > segundo_punto

    def __eq__(self, otro_punto):
        # Sobrecargar el metodo '=='
        return self.x == otro_punto.x and self.y == otro_punto.y 
    
    def calcularPuntos(self,equipo,partido):
        
        if partido == 'local':
            
            if equipo.getcantGolesLocal() > equipo.getcantGolesVisitante():
                
                return 3
            elif equipo.getcantGolesLocal() < equipo.getcantGolesVisitante():
                
                return 0
            
            else: return 1
            
        elif partido == 'visitante':
     
            if equipo.getcantGolesLocal() < equipo.getcantGolesVisitante():
            
                return 3
            elif equipo.getcantGolesLocal() > equipo.getcantGolesVisitante():
                
                return 0
            
            else: return 1
            
    def listadoPartidosPorId(self,idEquipo):
        
        
        i = 0
        golesAfavor = 0
        golesEncontra = 0
        difGoles = 0
        puntos = 0
        while i<len(self.__listFechas):
            
            if self.__listFechas[i].getIdEquipoLocal() == idEquipo:
                
                
                print("{}\t{}\t\t{}\t\t{}\t\t\t{}".format(self.__listFechas[i].getFechaPartido(),self.__listFechas[i].getcantGolesLocal(),self.__listFechas[i].getcantGolesVisitante(),int(self.__listFechas[i].getcantGolesLocal())-int(self.__listFechas[i].getcantGolesVisitante()),self.calcularPuntos(self.__listFechas[i],'local')))
                golesAfavor = golesAfavor + self.__listFechas[i].getcantGolesLocal()
                golesEncontra = golesEncontra + self.__listFechas[i].getcantGolesVisitante()
                difGoles = difGoles + (golesAfavor-golesEncontra)
                puntos = puntos + self.calcularPuntos(self.__listFechas[i],'local')
            elif self.__listFechas[i].getIdEquipoVisitante() == idEquipo:
                
                print("{}\t{}\t\t{}\t\t{}\t\t\t{}".format(self.__listFechas[i].getFechaPartido(),self.__listFechas[i].getcantGolesVisitante(),self.__listFechas[i].getcantGolesLocal(),int(self.__listFechas[i].getcantGolesVisitante())-int(self.__listFechas[i].getcantGolesLocal()),self.calcularPuntos(self.__listFechas[i],'visitante')))
                golesAfavor = golesAfavor + self.__listFechas[i].getcantGolesVisitante()
                golesEncontra = golesEncontra + self.__listFechas[i].getcantGolesLocal()
                difGoles = difGoles + (golesEncontra-golesAfavor)
                puntos = puntos + self.calcularPuntos(self.__listFechas[i],'visitante')
            
            i = i+1
        print("Totales: \t{}\t\t{}\t\t{}\t\t\t{}".format(golesAfavor,golesEncontra,difGoles,puntos))
    
    def calcularFechas(self,idEquipo):
        
        i = 0
        totalGolesafavor = 0
        totalGolesencontra = 0
        totalDifgoles = 0
        totalpuntos = 0
        
        while i<len(self.__listFechas):
            
            if self.__listFechas[i].getIdEquipoLocal() == idEquipo:
                
                totalGolesafavor = totalGolesafavor + self.__listFechas[i].getcantGolesLocal()
                totalGolesencontra = totalGolesencontra + self.__listFechas[i].getcantGolesVisitante()
                totalDifgoles = totalDifgoles + (totalGolesafavor-totalGolesencontra)
                totalpuntos = totalpuntos + self.calcularPuntos(self.__listFechas[i],'local')
            
            elif self.__listFechas[i].getIdEquipoVisitante() == idEquipo:
                
                totalGolesafavor = totalGolesafavor + self.__listFechas[i].getcantGolesVisitante()
                totalGolesencontra = totalGolesencontra + self.__listFechas[i].getcantGolesLocal()
                totalDifgoles = totalDifgoles + (totalGolesencontra-totalGolesafavor)
                totalpuntos = totalpuntos + self.calcularPuntos(self.__listFechas[i],'visitante')
            
            i = i+1
        return totalGolesafavor,totalGolesencontra,totalDifgoles,totalpuntos