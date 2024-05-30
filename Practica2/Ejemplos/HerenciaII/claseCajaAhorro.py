from claseCuenta import Cuenta

class CajaAhorro(Cuenta):

    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)

    def imprimir(self):
        print("Cuenta de Caja de Ahorro")
        super().imprimir()