import msvcrt
import funciones
class GestorVentas:

    __ventas = []

    def __init__(self,cantSuc,cantDias):
        
        for i in range(cantSuc): #5 Sucursales
            self.__ventas.append([i]*cantDias) #7 Dias

            for y in range(cantDias):
                
                self.__ventas[i][y] = 0
        


    def cargarVentas(self,sucursal,dia,importe):
        
        self.__ventas[sucursal-1][dia-1] += importe


    def totalFacturadoPorSucursal(self,sucursal):
        
        total = 0
        for i in range(len(self.__ventas)):
            
            
            total += self.__ventas[sucursal-1][i]
        
        print("Total Facturado de la Sucursal {} fue de {}".format(sucursal,total))
        msvcrt.getch() 
    
    def sucursalMenosFacturoDelDia(self,dia):
        
        min = 10000
        for i in range(len(self.__ventas)):
            
            if(self.__ventas[i][dia-1] < min):
                
                min = self.__ventas[i][dia-1]
                suc = i+1
        
        
        print("El dia {} la Sucursal que Menos Facturo fue la Sucursal {} con un Total ${}".format(funciones.dia(dia),suc,min))
      
    
    def sucursalMenosFacturoDeLaSemana(self):
        
        min = 100000
        
        
        for i in range(len(self.__ventas)):
            
            if(funciones.minimo(self.__ventas,i)<min):
                
                min = funciones.minimo(self.__ventas,i)
                
                suc = i+1
        
        print("La Sucursal que Menos Facturo en la Semana fue la Sucursal {} con un Total de ${}".format(suc,min))
                
    def totalFacturadoDeLaSemana(self):
        
        total = 0
        
        for i in range(len(self.__ventas)):
            
            total += funciones.minimo(self.__ventas,i)
        
        print("Total Facturado de la Semana: ", total)
                  