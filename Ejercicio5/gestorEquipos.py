import csv

from equipo import Equipo

class GestorEquipos:

    __listEquipos : list

    def __init__(self):
        
        self.__listEquipos = []

    def agregarEquipos(self,nuevoEquipo):

        self.__listEquipos.append(nuevoEquipo)

    def cargarListaEquipos(self):
        
        
        archiEquipos = open('equipos2024.csv')
        readerEquipo = csv.reader(archiEquipos,delimiter=',')    
        
        for fila in readerEquipo:
            
            idequipo = fila[0]
            nomequipo = fila[1]
            golesafavor = fila[2]
            golesencontra = fila[3]
            difgoles = fila[4]
            puntos = fila[5]
            nuevoEquipo = Equipo(idequipo,nomequipo,golesafavor,golesencontra,difgoles,puntos)
            self.agregarEquipos(nuevoEquipo)
        
        archiEquipos.close()
        
    def __gt__(self, otro_punto):
        # Sobrecargar el metodo '>'
        # Comparar las puntos de los primeros equipos de cada gestor
        # Obtener los puntos del primer equipo del gestor actual
        puntos_gestor_actual = self.__listEquipos[0].getPuntos()
        # Obtener los puntos del primer equipo del otro gestor
        puntos_otro_gestor = otro_punto.__listEquipos[0].getPuntos()
        # Comparar las puntos y devolver el resultado (True o False)
        return puntos_gestor_actual > puntos_otro_gestor
    
    def mostrar(self):

        for i in range(len(self.__listEquipos)):

            print(self.__listEquipos[i])

    def buscar(self,nombrequipo):

        i = 0

        while i< len(self.__listEquipos) and self.__listEquipos[i].getNomEquipo() != nombrequipo:

            i = i+1
        

        if self.__listEquipos[i].getNomEquipo() == nombrequipo:

            return self.__listEquipos[i].getIdEquipo()
        
        else:
            
            print("No existe un equipo con ese Nombre!")


    def actualizarLista(self,gfechas):
        
        for i in range(len(self.__listEquipos)):
            
            #Obtengo el total de goles a favor,en contra,dif goles y puntos de un equipo
            nuevoGolesAfavor,nuevoGolesEncontra,nuevoDifgoles,nuevoPuntos = gfechas.calcularFechas(self.__listEquipos[i].getIdEquipo())
            
            #Lo cambio de la lista Equipo mediante el metodo set de cada variable
            self.__listEquipos[i].setGolesAFavor(nuevoGolesAfavor+self.__listEquipos[i].getGolesAFavor())
            self.__listEquipos[i].setGolesEnContra(nuevoGolesEncontra+self.__listEquipos[i].getGolesEnContra())
            self.__listEquipos[i].setDiferenciaGoles(nuevoDifgoles+self.__listEquipos[i].getDiferenciaGoles())
            self.__listEquipos[i].setPuntos(nuevoPuntos+self.__listEquipos[i].getPuntos())
    
    
    def ordenarLista(self):
        
        #self.__listEquipos.sort(key=lambda equipos: equipos.getPuntos(),reverse = True)
        #reverse = True - Funciona como para ordenar de mayor a menor
        
        self.__listEquipos.sort(key=lambda equipo: (equipo.getPuntos(),equipo.getDiferenciaGoles() ,equipo.getGolesAFavor(), equipo.getGolesAFavor()), reverse=True)
        #self.__listEquipos.sort(key=lambda equipo: (equipo.getPuntos(), equipo.getGolesAFavor(), equipo.getGolesEnContra()), reverse=True)
        # De esta forma el metodo sort ordenaria por prioridad por Puntos luego si tienen la misma cantidad de puntos,verifica la diferencia de goles, y si es igual por goles a favor
        
        
    def actualizarArchivo(self):
        # Abrir el archivo CSV en modo lectura
        with open('equipos2024.csv', 'r', newline='') as archivoEquipo_Lectura: #Archivo Abierto para Lectura
            readerEquipo = csv.reader(archivoEquipo_Lectura)
            datos_del_archivo = list(readerEquipo)  # Leer los datos del archivo csv y lo convierte en una lista
            
            # Método para obtener los atributos del equipo como una lista
            datos_nuevos_lista = [equipo.obtener_datos_como_lista() for equipo in self.__listEquipos]
            
            # Modificar los datos originales con los datos actualizados de la lista
            for i, fila in enumerate(datos_del_archivo):
                datos_del_archivo[i] = datos_nuevos_lista[i]  #Modifica toda una linea del archivo con un bloque completo de la lista
            
            # Escribir los datos actualizados de vuelta al archivo csv
            with open('equipos2024.csv', 'w', newline='') as archivoEquipo_Escritura:#Archivo Abirto para Escritura
                writerEquipo = csv.writer(archivoEquipo_Escritura)
                writerEquipo.writerows(datos_del_archivo)