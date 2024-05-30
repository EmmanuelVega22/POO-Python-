from abc import ABC, abstractmethod

class InterfaceColeccion(ABC):
    @abstractmethod
    def insertarElemento(self, elemento, posicion):
        """Inserta un objeto en una posición determinada en la colección."""
        pass

    @abstractmethod
    def agregarElemento(self, elemento):
        """Agrega un elemento al final de la colección."""
        pass

    @abstractmethod
    def mostrarElemento(self, posicion):
        """Muestra los datos del elemento almacenado en la posición especificada."""
        pass

class Coleccion(InterfaceColeccion):
    def __init__(self):
        self.coleccion = []

    def insertarElemento(self, elemento, posicion):
        try:
            if posicion < 0 or posicion > len(self.coleccion):
                raise IndexError("Posición inválida")
            self.coleccion.insert(posicion, elemento)
        except IndexError as e:
            print(f"Error: {e}")

    def agregarElemento(self, elemento):
        self.coleccion.append(elemento)

    def mostrarElemento(self, posicion):
        try:
            if posicion < 0 or posicion >= len(self.coleccion):
                raise IndexError("Posición inválida")
            print(self.coleccion[posicion])
        except IndexError as e:
            print(f"Error: {e}")

# Ejemplo de uso
coleccion = Coleccion()
coleccion.agregarElemento("Elemento 1")
coleccion.agregarElemento("Elemento 2")
coleccion.insertarElemento("Nuevo elemento", 1)  # Inserta en la posición 1
coleccion.mostrarElemento(0)  # Muestra el elemento en la posición 0
coleccion.mostrarElemento(2)  # Muestra el elemento en la posición 2
coleccion.mostrarElemento(3)  # Intenta mostrar un elemento en una posición no válida
