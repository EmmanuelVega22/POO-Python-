class Equipo:

    __idEquipo : str
    __nomEquipo : str
    __golesAFavor: int
    __golesEnContra: int
    __diferenciaGoles: int
    __puntos : int

    def __init__(self,idequipo,nomequipo,golesafavor,golesencontra,diferenciagoles,puntos):
        
        self.__idEquipo = idequipo
        self.__nomEquipo = nomequipo
        self.__golesAFavor = golesafavor
        self.__golesEnContra = golesencontra
        self.__diferenciaGoles = diferenciagoles
        self.__puntos = puntos
        
    def __str__(self):
        
        return "%s %s %s %s %s %s" % (self.__idEquipo, self.__nomEquipo, self.__golesAFavor, self.__golesEnContra, self.__diferenciaGoles,self.__puntos)
   
    
    def obtener_datos_como_lista(self):
        return [self.__idEquipo, self.__nomEquipo, self.__golesAFavor,self.__golesEnContra,self.__diferenciaGoles,self.__puntos]
    
    def getNomEquipo(self):

        return self.__nomEquipo
    
    def getIdEquipo(self):
        
        return self.__idEquipo
    
    def getGolesAFavor(self):
        
        return int(self.__golesAFavor)
    
    def setGolesAFavor(self,nuevo):
        
        self.__golesAFavor = nuevo
    
    def getGolesEnContra(self):
        
        return int(self.__golesEnContra)
    
    def setGolesEnContra(self,nuevo):
        
        self.__golesEnContra = nuevo
    
    def getDiferenciaGoles(self):
        
        return int(self.__diferenciaGoles)
    
    def setDiferenciaGoles(self,nuevo):
        
        self.__diferenciaGoles = nuevo
    
    def getPuntos(self):
        
        return int(self.__puntos)
    
    def setPuntos(self,nuevo):
        
        self.__puntos = nuevo