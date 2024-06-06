
class Nodo:

    __planes:object
    __siguiente: object

    def __init__(self,plan):

        self.__planes = plan
        self.__siguiente = None

    
    def getSiguiente(self):

        return self.__siguiente
    
    def setSiguiente(self,siguiente):

        self.__siguiente = siguiente

    def getDato(self):

        return self.__planes