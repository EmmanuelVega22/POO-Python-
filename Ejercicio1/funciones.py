# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""


import clase
def test(lista):
    
    for i in range(3):
        nom = input("Ingrese Nombre: ")
        apell = input("Ingrese Apellido: ")
        nroc = input("Ingrese Nro de Cuenta: ")
        cuit = input("Ingrese CUIT: ")
        saldo = float(input("Ingrese Saldo: "))
    
        c = clase.CajaDeAhorro(nroc,nom,apell,cuit,saldo)
    
        lista.append(c)
    
    for i in range(len(lista)):
        
        lista[i].mostrarDatos()
    
    print(" ____________")
    print("| EXTRAER    |")
    print("|____________|")
    
    nrocuenta = input("Ingrese Nro de su Cuenta: ")
    
    b = False
    for y in range(len(lista)):
        
        if lista[y].getnroCuenta() == nrocuenta:
            
            b = True
            monto = float(input("Ingrese el Monto que desea Extraer: "))
            if lista[y].extraer(monto) == -1:
            
                print("No tiene Saldo Suficiente. Excede su Saldo")
            
            else:
                
                print("Extraccion Exitosa. Nuevo Saldo: ", lista[y].getSaldo())
            
            break
    
    if b == False:
        
        print("No existe ese Nro de Cuenta!")
    
    
    print(" ____________")
    print("| DEPOSITAR  |")
    print("|____________|")
    
    nrocuenta = input("Ingrese Nro de su Cuenta: ")
    
    for y in range(len(lista)):
        
        if lista[y].getnroCuenta() == nrocuenta:
            
            importe = float(input("Ingrese el Importe que desea Depositar: "))
            
            if importe < 1:
            
                print("Error! Importe ingresado es Negativo")
            
            else:
                
                lista[y].depositar(importe)
                
                print("Deposito Exitoso. Nuevo Saldo: ", lista[y].getSaldo())
            
            break
    
    print(" ______________")
    print("| VALIDAR CUIL |")
    print("|______________|")
    
    
    dato = input("Ingrese su CUIL: ")
    
    c.validarCUIL(dato)