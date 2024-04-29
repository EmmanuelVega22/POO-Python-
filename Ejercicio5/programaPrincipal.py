import funciones
from gestorEquipos import GestorEquipos
from gestorFechaFutbol import GestorFechaFutbol

if __name__=='__main__':


    ge = GestorEquipos()
    gf = GestorFechaFutbol()
    
    op = 0 

    while op != '7':

        op = funciones.menu()

        if op == '1':

            ge.cargarListaEquipos()
            ge.mostrar()

        elif op == '2':
            
            gf.cargarListaFechas()
            gf.mostrar()

        elif op == '3':
            
            funciones.listado(ge,gf)

        elif op == '4':
            
            ge.actualizarLista(gf)
            ge.mostrar()
            
        elif op == '5':
            
            ge.ordenarLista()
            ge.mostrar()
            
        elif op == '6':
            
            ge.actualizarArchivo()