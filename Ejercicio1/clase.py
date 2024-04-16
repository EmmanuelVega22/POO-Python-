# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:15:32 2024

@author: Emmanuel
"""

class CajaDeAhorro:
    
    __nroCuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float
    
    
    def __init__(self,nroC,nombre,apellido,cuil,saldo):
        
        self.__nroCuenta = nroC
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuil = cuil
        self.__saldo = saldo
    
    
    
    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self,nuevoSaldo):
        
        self.__saldo = nuevoSaldo
    
    def getnroCuenta(self):
        return self.__nroCuenta
    
    def mostrarDatos(self):
           
        print("_______________")
        print("|Caja de Ahorro|")
        print("|______________|")
        print("Nro Cuenta: ", self.__nroCuenta)
        print("Nombre: ", self.__nombre)
        print("Apellido: ", self.__apellido)
        print("CUIL: ", self.__cuil)
        print("Saldo: $", self.__saldo)
            
    def extraer(self,monto):
        
        if (self.getSaldo()-monto)<0:
           
           return -1
       
        else:
            
           self.setSaldo(self.getSaldo()-monto)
           
           return self.getSaldo()-monto
     
    def depositar(self,importe):
            
            nuevosaldo = self.getSaldo() + importe
            
            self.setSaldo(nuevosaldo)
            
    
    def validarCUIL(self,dato):
        
        if len(dato)!=13:
            
            print("Cuil Ingresado Incorrecto.(13 Caracteres)")
            return False
        
        else:
            
            partes = dato.split('-')
            
            
            parte2 = partes[0]+""+partes[1]
    
            total = 0 
 
            print(parte2)
            num = 5
            for i in range(len(parte2)):
        
                if num != 1:
            
                    total = total + int(parte2[i])*num
                    num = num-1
            
                else:
            
                    num = 7
                    total = total + int(parte2[i])*num
                    num = num-1
            
            resto = total%11
            
            if resto-11 == 0:
        
                if resto-11 == partes[2]:
                    
                    partes[2] = resto
                else:
                    return False
            
            elif resto-11 == 1:
                
                if partes[0] == 20:
                    
                    partes[2] = 9
                    partes[0] = 23

                
                elif partes[0] == 27:
                    
                    partes[2] = 4
                    partes[0] = 23
                    
            
            else:
                
                partes[2] = 11-resto
            
        return True