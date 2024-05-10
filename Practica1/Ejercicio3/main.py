from GestorVentas import GestorVentas
import funciones
import msvcrt #Pausar pantalla
import os #limpiar pantalla

if __name__ == '__main__':

    ventas = GestorVentas(5,7)
    
    op = 0
    while op !='6':
        
        os.system('cls')
        op = funciones.menu()
        if op == '1':

            sucursal =  int(input("Ingrese Nro Sucursal (1 al 5): "))
            dia = int(input("Ingrese Dia de la Semana (1 al 7): "))
            importe = float(input("Ingrese importe de Facturacion de ese dia: "))
            os.system('cls')
            ventas.cargarVentas(sucursal,dia,importe)

        elif op == '2':
            
            sucursal = int(input("Ingrese Nro de Sucural (1 al 5): "))
            os.system('cls')
            ventas.totalFacturadoPorSucursal(sucursal)

        elif op == '3':
            dia = int(input("Ingrese Dia de la Semana (1 al 7): "))
            
            ventas.sucursalMenosFacturoDelDia(dia)
            
        elif op == '4':
            
            ventas.sucursalMenosFacturoDeLaSemana()
            
        elif op == '5':
            
            ventas.totalFacturadoDeLaSemana()