
from clasePlanTelefonia import PlanTelefonia
from clasePlanTelevision import PlanTelevision
from claseNodo import Nodo
import csv

class Lista:

    __cabeza: Nodo
    __actual: Nodo
    __indice = 0
    __tope = 0


    def __init__(self):

        self.__cabeza = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    
    def __iter__(self):

        return self
    
    def __next__(self):

        if self.__indice == self.__tope:

            self.__actual = self.__cabeza
            self.__indice = 0
            raise StopIteration
        
        else:

            self.__indice +=1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()

            return dato
    
    def cargarLista(self):

        archivoPlanes = open("planes.csv")
        readerArchivo = csv.reader(archivoPlanes,delimiter=',')

        for fila in readerArchivo:
            
            tipo_de_plan = fila[0]
            
            if tipo_de_plan == 'M':

                nuevoPlan = PlanTelefonia(*fila[1:])

            elif tipo_de_plan == 'T':

                nuevoPlan = PlanTelevision(*fila[1:])
            
            nodo = Nodo(nuevoPlan)

            if self.__cabeza == None:

                self.__cabeza =  nodo
                self.__actual = nodo
                self.__tope +=1
            
            else:

                aux = self.__cabeza

                while aux.getSiguiente() != None:

                    aux = aux.getSiguiente()
                
                aux.setSiguiente(nodo)
                self.__actual = self.__cabeza
                self.__tope +=1
    

    def mostrar(self):

        aux = self.__cabeza

        while aux != None:

            print(aux.getDato())
            aux = aux.getSiguiente()


    def mostrarTipoDeDatoPorPosicion(self,posicion):

        indice = 0
        aux = self.__cabeza

        while aux != None:

            if 0 <= posicion < self.__tope:
                if indice == posicion:

                    if isinstance(aux.getDato(),PlanTelefonia):

                        print("En la posicion {} se encuentra un objeto de tipo Plan Telefonia".format(posicion))
                        break
                    elif isinstance(aux.getDato(),PlanTelevision):

                        print("En la posicion {} se encuentra un objeto de tipo Plan Television".format(posicion))
                        break
                indice +=1
                aux = aux.getSiguiente()
            else:

                return IndexError("Indice fuera de rango")

    def mostrarCantidadDePlanesConCobertura(self,cobertura):
        
        cantTelefonia = 0
        cantTelevision = 0
        aux = self.__cabeza

        while aux != None:

            if aux.getDato().getCoberturaGeografica() == cobertura:

                if isinstance(aux.getDato(),PlanTelefonia):

                    cantTelefonia +=1

                elif isinstance(aux.getDato(),PlanTelevision):

                    cantTelevision+=1
            
            aux = aux.getSiguiente()

        print("La cantidad de Plan Telefonia con Cobertura Geografica {} son {}".format(cobertura,cantTelefonia))
        
        print("La cantidad de Plan Television con Cobertura Geografica {} son {}".format(cobertura,cantTelevision))


    
    def mostrarCantidadDeCanalesInternacionales(self,canales):


        aux = self.__cabeza

        while aux != None:

            if isinstance(aux.getDato(),PlanTelevision):

                if int(aux.getDato().getCanalesInternacionales()) >= canales:

                    print("Compania: {} \n".format(aux.getDato().getNombreCompania()))

            aux = aux.getSiguiente()

    def mostrarDatosDeLaLista(self):


        aux = self.__cabeza

        while aux != None:

            if isinstance(aux.getDato(),PlanTelefonia):

                print("TIpo de Plan: Plan Telefonia")
                print("Nombre Compania: ", aux.getDato().getNombreCompania())
                print("Duracion de Plan: ", aux.getDato().getDuracionPlan())
                print("Cobertura Geografica: ", aux.getDato().getCoberturaGeografica())
                print("Importe Final: ", aux.getDato().importeDePlan())

            elif isinstance(aux.getDato(),PlanTelevision):

                print("Tipo de Plan: Plan Television")
                print("Nombre Compania: ", aux.getDato().getNombreCompania())
                print("Duracion de Plan: ", aux.getDato().getDuracionPlan())
                print("Cobertura Geografica: ", aux.getDato().getCoberturaGeografica())
                print("Importe Final: ", aux.getDato().importeDePlan())

            aux = aux.getSiguiente()
