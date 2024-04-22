class GestorMotos:

    __listMotos : list

    def __init__(self):
        
        self.__listMotos = []

    
    def agregarMotos(self,newMoto):

        self.__listMotos.append(newMoto)