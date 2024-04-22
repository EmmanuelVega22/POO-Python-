import csv
from Moto import Moto
from Pedidos import Pedido

from GestorPedidos import GestorPedidos
from GestorMotos import GestorMotos

def cargarMotos():

    newgestorMotos = GestorMotos()
    archivoMotos = open('datosMotos.csv')
    readerMotos = csv.reader(archivoMotos,delimiter=';')
    
    for fila in readerMotos:

        newgestorMotos.agregarMotos(fila)
    
    archivoMotos.close()

def cargarPedidos():

    newgestorPedido = GestorPedidos()

    archivoPedidos = open('datosPedidos.csv')
    readerPedidos = csv.reader(archivoPedidos,delimiter=';')
    
    for fila in readerPedidos:
        
        newgestorPedido.agregarPedido(fila)

    archivoPedidos.close()


def cargarNuevosPedidos():
    
    gp = GestorPedidos()

    patente = input("Patente:")
    i = 0

    while i < len(gp.getList()) and patente != gp.getList[i].getPatente():
        #busca que la patente exista
        pass

    #if para saber si lo encontro o no
    #si lo encontro agrega un nuevo pedido
    #un pedido = pedido()
    #gestorpedidos.append(un pedido)