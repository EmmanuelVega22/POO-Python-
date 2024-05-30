import msvcrt

from claseCajaAhorro import CajaAhorro
from clasePlazoFijo import PlazoFijo

if __name__ == '__main__':
    
    
    cjahorro = CajaAhorro("Mario", 2000)
    cjahorro.imprimir()

    plazofijo = PlazoFijo("Juana", 10000, 30, 0.75)
    plazofijo.imprimir()
    
    msvcrt.getch()
    

