import funciones
from gestorEquipos import GestorEquipos
from gestorFechaFutbol import GestorFechaFutbol
from equipo import Equipo
if __name__=='__main__':

    pass
    #C)_buscar(metodo buscar) en gestor equipo el nombre del equipo
    #y guardar el idquipo, luego buscar en GestorPartido con
    # un metodo buscar,con idequipo
    #Contar como id de equipo visitante y id de equipo local
    #4)_ def actualizar el archivo con la tabla de equipo en el archivo (puntos)
    #5)_ ordenar la tabla(osea la tabla) sobrecargar el operador mayor que
    #6)_ 

    ge = GestorEquipos()
    gf = GestorFechaFutbol()
    
    op = 0
    
    while op != '7':

        op = funciones.menu()

        if op == '1':

            ge.cargarLista()

        elif op == '2':
            gf.cargarLista()

        elif op == '3':
            
            nombre = input("Ingrese Nombre del Equipo: ")
            #ge.buscar(nombre)

            Equipo.getNomEquipo()
        elif op == '4':

            pass
        elif op == '5':
            pass
        elif op == '6':
            pass

