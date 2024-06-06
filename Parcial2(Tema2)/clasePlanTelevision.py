
from claseTelecomunicaciones import Telecomunicaciones


class PlanTelevision(Telecomunicaciones):

    __cantidad_canales_nacionales:int
    __cantidad_canales_internacionales:int


    def __init__(self,nombre,duracion,cobertura,precio,canales_nacionales,canales_internacionales):

        super().__init__(nombre,duracion,cobertura,precio)

        self.__cantidad_canales_nacionales = canales_nacionales
        self.__cantidad_canales_internacionales = canales_internacionales

    def __str__(self):

        cadena = super().__str__()
        cadena += "Cantidad de Canales Nacionales: " + str(self.__cantidad_canales_internacionales) + "\n"
        cadena += "Cantidad de Canales Internacionales: " + str(self.__cantidad_canales_internacionales) + "\n"

        return cadena
    
    
    def getCanalesNacionales(self):

        return self.__cantidad_canales_nacionales
    

    def getCanalesInternacionales(self):

        return self.__cantidad_canales_internacionales
    

    def importeDePlan(self):

        if int(self.getCanalesInternacionales()) > 10:

            importe = float(self.getPrecioBase()) + (float(self.getPrecioBase()) * 1.15)

            return importe
        
