
from claseNodo import Nodo
from claseLibro import Libro
from claseCD import CD
class Lista:

    __comienzo = Nodo


    def __init__(self):

        self.__comienzo = None

    def cargarPublicaciones(self):

        if self.__comienzo == None:

            titulo = input("Ingrese Titulo: ")
            categoria = input("Ingrese Categoria: ")
            precio_base = float(input("Ingrese Precio Base: "))

            op = input("¿Es un libro o CD? (L/C)")

            if op == 'L':

                autor = input("Ingrese Nombre Autor: ")
                fecha = input("Ingrese Fecha de Edicion: ")
                paginas = int(input("Ingrese Cantidad de Paginas: "))

                nuevoLibro = Libro(titulo,categoria,precio_base,autor,fecha,paginas)
                nodo = Nodo(nuevoLibro)
            elif op == 'C':

                tiempo_reprod = int(input("Ingrese Tiempo Reproduccion en minutos: "))
                narrador = input("Ingrese Narrador: ")

                nuevoCD = CD(titulo,categoria,precio_base,tiempo_reprod,narrador)
                nodo = Nodo(nuevoCD)
            
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            print("Cargador Exitosamente LIsta Vacias")
        
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:

                aux = aux.getSiguiente()
            
            titulo = input("Ingrese Titulo: ")
            categoria = input("Ingrese Categoria: ")
            precio_base = input("Ingrese Precio Base: ")

            op = input("¿Es un libro o CD? (L/C)")

            if op == 'L':

                autor = input("Ingrese Nombre Autor: ")
                fecha = input("Ingrese Fecha de Edicion: ")
                paginas = input("Ingrese Cantidad de Paginas: ")

                nuevoLibro = Libro(titulo,categoria,precio_base,autor,fecha,paginas)
                nodo = Nodo(nuevoLibro)
            elif op == 'C':

                tiempo_reprod = input("Ingrese Tiempo Reproduccion en minutos: ")
                narrador = input("Ingrese Narrador: ")

                nuevoCD = CD(titulo,categoria,precio_base,tiempo_reprod,narrador)
                nodo = Nodo(nuevoCD)
            
            aux.setSiguiente(nodo)
            nodo.setSiguiente(aux.getSiguiente())
            print("Cargador Exitosamente LIsta No Vacias")


    def mostrar(self):

        aux = self.__comienzo

        while aux!=None:

            print(aux.getDato())
            aux=aux.getSiguiente()
        

