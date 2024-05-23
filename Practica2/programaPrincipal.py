
from datetime import datetime
from claseLista import Lista
from menu import menu
if __name__ == '__main__':

    
    clista = Lista()


    op = 0

    while op != '2':

        op = menu()
        if op == '1':

            clista.cargarPublicaciones()
            clista.mostrar()
        