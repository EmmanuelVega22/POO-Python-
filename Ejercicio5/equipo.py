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


    def getNomEquipo(self):

        return self.__nomEquipo
    
