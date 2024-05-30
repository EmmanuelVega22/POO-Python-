from zope.interface import Interface, implementer

class IProducto(Interface):
    def modificarPrecio(self, precio):
        """Modifica el precio del producto."""
        pass

    def getDescripcion(self):
        """Obtiene la descripción del producto."""
        pass

    def getCodigo(self):
        """Obtiene el código del producto."""
        pass

@implementer(IProducto)
class Producto:
    def __init__(self, codigo, descripcion, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio

    def modificarPrecio(self, precio):
        self.precio = precio

    def getDescripcion(self):
        return self.descripcion

    def getCodigo(self):
        return self.codigo

class ICajero(Interface):
    def buscarProductoPorDescripcion(self, descripcion):
        """Busca un producto por su descripción."""
        pass

    def modificarPrecio(self, codigo, precio):
        """Modifica el precio de un producto."""
        pass

@implementer(ICajero)
class ManejadorProductosCajero:
    def __init__(self, productos):
        self.productos = productos

    def buscarProductoPorDescripcion(self, descripcion):
        for producto in self.productos:
            if producto.getDescripcion() == descripcion:
                return producto
        return None

    def modificarPrecio(self, codigo, precio):
        for producto in self.productos:
            if producto.getCodigo() == codigo:
                producto.modificarPrecio(precio)
                return

class ISupervisor(Interface):
    def buscarProductoPorCodigo(self, codigo):
        """Busca un producto por su código."""
        pass

    def modificarPrecio(self, codigo, precio):
        """Modifica el precio de un producto."""
        pass

@implementer(ISupervisor)
class ManejadorProductosSupervisor:
    def __init__(self, productos):
        self.productos = productos

    def buscarProductoPorCodigo(self, codigo):
        for producto in self.productos:
            if producto.getCodigo() == codigo:
                return producto
        return None

    def modificarPrecio(self, codigo, precio):
        for producto in self.productos:
            if producto.getCodigo() == codigo:
                producto.modificarPrecio(precio)
                return

def supervisor(manejador_supervisor):
    codigo = int(input('Código del producto a cambiar precio: '))
    producto = manejador_supervisor.buscarProductoPorCodigo(codigo)
    if producto is None:
        print(f'No se encontró un producto con el código {codigo}')
    else:
        print(f'Producto encontrado: {producto.getDescripcion()}')
        nuevo_precio = float(input('Nuevo precio: '))
        manejador_supervisor.modificarPrecio(codigo, nuevo_precio)
        print(f'Precio modificado: {producto.precio}')

def cajero(manejador_cajero):
    descripcion = input('Descripción de producto a buscar: ')
    producto = manejador_cajero.buscarProductoPorDescripcion(descripcion)
    if producto is None:
        print(f'Producto "{descripcion}" no encontrado')
    else:
        print(f'Producto encontrado: {producto.getDescripcion()}')
        print(f'Precio: {producto.precio}')

def testInterfaces():
    productos = [
        Producto(1, 'Arroz 1kg', 52),
        Producto(2, 'Yerba 1/2kg', 120)
    ]

    manejador_cajero = ManejadorProductosCajero(productos)
    manejador_supervisor = ManejadorProductosSupervisor(productos)

    usuario = input('Usuario (Admin/Cajero): ')
    clave = input('Clave: ')

    if usuario.lower() == 'admin' and clave == 'a54321':
        supervisor(manejador_supervisor)
    elif usuario.lower() == 'cajero' and clave == 'c12345':
        cajero(manejador_cajero)
    else:
        print('Usuario o clave incorrectos')

if __name__ == '__main__':
    testInterfaces()
