
from claseNodo import Nodo
from claseLibro import Libro
from claseCD import CD
class Lista:

    __cabeza = Nodo


    def __init__(self):

        self.__cabeza = None

    def cargarPublicaciones(self):
        
        op = 'si'
        
        while op != 'NO':
            
            if self.__cabeza == None:
    
                titulo = input("Ingrese Titulo: ")
                categoria = input("Ingrese Categoria: ")
                precio_base = float(input("Ingrese Precio Base: "))
    
                tipo = input("¿Es un libro o CD? (L/C)").upper()
    
                if tipo == 'L':
    
                    autor = input("Ingrese Nombre Autor: ")
                    fecha = input("Ingrese Fecha de Edicion: ")
                    paginas = int(input("Ingrese Cantidad de Paginas: "))
    
                    publicacion = Libro(titulo,categoria,precio_base,autor,fecha,paginas)
                
                elif tipo == 'C':
    
                    tiempo_reprod = int(input("Ingrese Tiempo Reproduccion en minutos: "))
                    narrador = input("Ingrese Narrador: ")
    
                    publicacion = CD(titulo,categoria,precio_base,tiempo_reprod,narrador)
                
                nodo = Nodo(publicacion)
                self.__cabeza = nodo
                        
            else:
                aux = self.__cabeza

                while aux.getSiguiente() != None:
    
                    aux = aux.getSiguiente()
                
                titulo = input("Ingrese Titulo: ")
                categoria = input("Ingrese Categoria: ")
                precio_base = float(input("Ingrese Precio Base: "))
    
                tipo = input("¿Es un libro o CD? (L/C)").upper()
    
                if tipo == 'L':
    
                    autor = input("Ingrese Nombre Autor: ")
                    fecha = input("Ingrese Fecha de Edicion: ")
                    paginas = int(input("Ingrese Cantidad de Paginas: "))
    
                    publicacion = Libro(titulo,categoria,precio_base,autor,fecha,paginas)
    
                elif tipo == 'C':
    
                    tiempo_reprod = int(input("Ingrese Tiempo Reproduccion en minutos: "))
                    narrador = input("Ingrese Narrador: ")
    
                    publicacion = CD(titulo,categoria,precio_base,tiempo_reprod,narrador)
                
    
                nodo = Nodo(publicacion)
                aux.setSiguiente(nodo)
            
            op = input("Cargar otra publicacion? (Si/No)").upper()
            
    def mostrar(self):

        aux = self.__cabeza

        while aux!=None:

            print(aux.getDato())
            aux=aux.getSiguiente()
        

    def mostrar_tipo_publicaciones(self,posicion):
        
        contador = 0
        aux = self.__cabeza
        
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
        
        aux = self.__cabeza
        
        while aux != None:
            
            if isinstance(aux.getDato() ,Libro):#Pregunta si el nodo es de tipo Libro
                
                cant_libros +=1
            
            elif isinstance(aux.getDato(),CD ):#Pregunta si el nodo es de tipo CD
                
                cant_cd +=1
            
            aux = aux.getSiguiente()
            
        print("Cantidad de Libros Impresos: ", cant_libros)
        print("Cantidad de Cds: ", cant_cd)
        
    def mostrar_publicaciones_importe(self):
        
        aux = self.__cabeza
        
        while aux != None:
            
            print("Titulo: ", aux.getDato().getTitutlo())
            print("Categoria: ", aux.getDato().getCategoria())
            print("Importe Venta: ", aux.getDato().importeVenta())
            print("\n")
            
            aux = aux.getSiguiente()
