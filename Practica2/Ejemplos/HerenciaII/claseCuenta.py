class Cuenta:
    
    __titular = str
    __cantidad = int
    
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir(self):
        print("Titular:",self.titular)
        print("Monto:", self.cantidad)

