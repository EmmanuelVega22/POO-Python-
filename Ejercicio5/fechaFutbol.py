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
