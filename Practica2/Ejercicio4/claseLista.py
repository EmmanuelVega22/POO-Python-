
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

            op = input("¿Es un libro o CD? (L/C)").upper()

            if op == 'L':

                autor = input("Ingrese Nombre Autor: ")
                fecha = input("Ingrese Fecha de Edicion: ")
                paginas = int(input("Ingrese Cantidad de Paginas: "))

                publicacion = Libro(titulo,categoria,precio_base,autor,fecha,paginas)
            
            elif op == 'C':

                tiempo_reprod = int(input("Ingrese Tiempo Reproduccion en minutos: "))
                narrador = input("Ingrese Narrador: ")

                publicacion = CD(titulo,categoria,precio_base,tiempo_reprod,narrador)
            
            nodo = Nodo(publicacion)
            self.__comienzo=nodo
                    
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:

                aux = aux.getSiguiente()
            
            titulo = input("Ingrese Titulo: ")
            categoria = input("Ingrese Categoria: ")
            precio_base = float(input("Ingrese Precio Base: "))

            op = input("¿Es un libro o CD? (L/C)").upper()

            if op == 'L':

                autor = input("Ingrese Nombre Autor: ")
                fecha = input("Ingrese Fecha de Edicion: ")
                paginas = int(input("Ingrese Cantidad de Paginas: "))

                publicacion = Libro(titulo,categoria,precio_base,autor,fecha,paginas)

            elif op == 'C':

                tiempo_reprod = int(input("Ingrese Tiempo Reproduccion en minutos: "))
                narrador = input("Ingrese Narrador: ")

                publicacion = CD(titulo,categoria,precio_base,tiempo_reprod,narrador)
            

            nodo = Nodo(publicacion)
            aux.setSiguiente(nodo)


    def mostrar(self):

        aux = self.__comienzo

        while aux!=None:

            print(aux.getDato())
            aux=aux.getSiguiente()
        

    def mostrar_tipo_publicaciones(self,posicion):
        
        contador = 0
        aux = self.__comienzo
        
        while aux != None:
            
            if contador == posicion:
                
                if isinstance(aux.getDato(),Libro):
                    
                    print("La publicación en la posición", posicion, "es un libro.")

                elif isinstance(aux.getDato(),CD):
                    
                    print("La publicación en la posición", posicion, "es un audio-libro.")
                    
                return
            
            else:
                contador +=1
                aux = aux.getSiguiente()
    
    
    def mostrar_cantidad_publicaciones(self):
        
        cant_libros = 0
        cant_cd = 0
        
        aux = self.__comienzo
        
        while aux != None:
            
            if isinstance(aux.getDato() ,Libro):
                
                cant_libros +=1
            
            elif isinstance(aux.getDato(),CD ):
                
                cant_cd +=1
            
            aux = aux.getSiguiente()
            
        print("Cantidad de Libros Impresos: ", cant_libros)
        print("Cantidad de Cds: ", cant_cd)
        
    def mostrar_publicaciones_importe(self):
        
        aux = self.__comienzo
        
        while aux != None:
            
            print("Titulo: ", aux.getDato().getTitutlo())
            print("Categoria: ", aux.getDato().getCategoria())
            print("Importe Venta: ", aux.getDato().importeVenta())
            print("\n")
            
            aux = aux.getSiguiente()