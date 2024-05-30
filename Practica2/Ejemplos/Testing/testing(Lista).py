import unittest

class TestLista(unittest.TestCase):

    def setUp(self):
        # Método setUp que crea la lista y agrega elementos
        self.lista = [1, 2, 3, 4, 5]

    def test_agregar_elemento(self):
        # Verificar que agregó elementos a la lista
        self.lista.append(6)
        self.assertIn(6, self.lista)

    def test_lista_no_vacia(self):
        # Verificar que la lista no está vacía
        self.assertTrue(self.lista)

    def test_eliminar_elemento_intermedio(self):
        # Eliminar un elemento intermedio de la lista y verificar que lo eliminó
        elemento_intermedio = self.lista[2]
        self.lista.remove(elemento_intermedio)
        self.assertNotIn(elemento_intermedio, self.lista)

    def test_eliminar_primer_elemento(self):
        # Eliminar el primer elemento de la lista y verificar que lo eliminó
        primer_elemento = self.lista[0]
        self.lista.pop(0)
        self.assertNotIn(primer_elemento, self.lista)

    def test_eliminar_ultimo_elemento(self):
        # Eliminar el último elemento de la lista y verificar que lo eliminó
        ultimo_elemento = self.lista[-1]
        self.lista.pop()
        self.assertNotIn(ultimo_elemento, self.lista)

    def test_vaciar_lista(self):
        # Vaciar la lista y verificar que está vacía
        self.lista.clear()
        self.assertFalse(self.lista)


if __name__ == '__main__':
    unittest.main()
