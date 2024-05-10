class FechaFutbol:

    __fechaPartido: str
    __idEquipoLocal: int
    __idEquipoVisitante: int
    __cantGolesLocal: int
    __cantGolesVisitante: int

    def __init__(self,fechapartido,idequipolocal,idequipovisitante,cantgoleslocal,cantgolesvisitante):
        
        self.__fechaPartido = fechapartido
        self.__idEquipoLocal = idequipolocal
        self.__idEquipoVisitante = idequipovisitante
        self.__cantGolesLocal = cantgoleslocal
        self.__cantGolesVisitante = cantgolesvisitante
    
    def __str__(self):
        
        return "%s %s %s %s %s" % (self.__fechaPartido,self.__idEquipoLocal, self.__idEquipoVisitante, self.__cantGolesLocal,self.__cantGolesVisitante)
   
    def getIdEquipoLocal(self):
        
        return self.__idEquipoLocal
    
    def getIdEquipoVisitante(self):
        
        return self.__idEquipoVisitante
    
    def getcantGolesLocal(self):
        
        return int(self.__cantGolesLocal)
    
    def getcantGolesVisitante(self):
        
        return int(self.__cantGolesVisitante)
    
    def getFechaPartido(self):
        
        return self.__fechaPartido