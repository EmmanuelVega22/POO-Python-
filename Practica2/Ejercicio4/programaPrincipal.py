from claseLista import Lista
from menu import menu
if __name__ == '__main__':

    
    clista = Lista()


    op = 0

    while op != '5':

        op = menu()
        if op == '1':

            clista.cargarPublicaciones()
            clista.mostrar()
        
        elif op == '2':
            
            posicion = int(input("Ingrese una posicion: "))
            
            clista.mostrar_tipo_publicaciones(posicion)
        
        elif op == '3':
            
            clista.mostrar_cantidad_publicaciones()
        
        elif op == '4':
            
            clista.mostrar_publicaciones_importe()