from claseCuenta import Cuenta

class PlazoFijo(Cuenta):
    
    __plazo = int
    __interes = float
    
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo=plazo
        self.interes=interes

    def imprimir(self):
        print("Cuenta de Plazo Fijo")
        super().imprimir()
        print("Plazo en dias:",self.plazo)
        print("Interes:",self.interes)
        self.ganancia_interes()

    def ganancia_interes(self):
        ganancias=self.cantidad*self.interes/100
        print("Importe del interes:",ganancias)