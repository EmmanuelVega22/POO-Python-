
from claseTelecomunicaciones import Telecomunicaciones

class PlanTelefonia(Telecomunicaciones):

    __tipo_llamadas:str
    __cant_minutos:int


    def __init__(self,nombre,duracion,cobertura,precio,tipo_llamada,cant_minutos):

        super().__init__(nombre,duracion,cobertura,precio)

        self.__tipo_llamadas = tipo_llamada
        self.__cant_minutos = cant_minutos

    def __str__(self):

        cadena = super().__str__()
        cadena += 'Tipo Llamadas: ' + self.__tipo_llamadas + '\n'
        cadena += 'Cantidad de Minutos: ' + str(self.__cant_minutos) + '\n'

        return cadena
    
    def getTipoLlamadas(self):

        return self.__tipo_llamadas
    
    def getCantMinutos(self):

        return self.__cant_minutos
    
    def importeDePlan(self):

        if self.getTipoLlamadas() == 'Internacionales':

            importe = float(self.getPrecioBase()) + (float(self.getPrecioBase()) * 1.20)

            return importe
        
        elif self.getTipoLlamadas() == 'Locales':

            importe = float(self.getPrecioBase()) - (float(self.getPrecioBase()) * 0.7)

            return importe