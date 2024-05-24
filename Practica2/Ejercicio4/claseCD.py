
from clasePublicaciones import Publicaciones

class CD(Publicaciones):

    __tiempo_reproduccion: int
    __narrador: str

    def __init__(self,titulo,categoria,precio_base,tiempo_reprod,narrador):
        
        super().__init__(titulo,categoria,precio_base)

        self.__tiempo_reproduccion = tiempo_reprod
        self.__narrador = narrador

    def __str__(self):

        cadena = super().__str__()
        cadena += 'CD:\n'
        cadena += 'TiempoReproduccion :'+ str(self.__tiempo_reproduccion)+'\n'
        cadena += 'Narrador:'+(self.__narrador)+'\n'

        return cadena
        
    def getTiempoReproduccion(self):

        return self.__tiempo_reproduccion
    
    def getNarrador(self):

        return self.__narrador
    

    def importeVenta(self):
        

        regalias = self.getPrecioBase() * 0.10
        
        return self.getPrecioBase() + regalias
