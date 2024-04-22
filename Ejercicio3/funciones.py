def menu():

    print("1_Registrar Ventas.")
    print("2_Total Facturado de Sucursal.")
    print("3_Sucursal que menos Facturo.")
    print("4_Sucursal Menos Facturo.")
    print("5_Total Facturado de la Semana.")
    print("6_Salir")
    op = input("Ingrese una Opcion:")
    
    return op

def dia(num):
    
    if num == 1:
        
        return 'Lunes'
    
    elif num == 2:
        
        return 'Martes'
    
    elif num == 3:
        
        return 'Miercoles'
        
    elif num == 4:
        
        return 'Jueves'
    
    elif num == 5:
        
        return 'Viernes'
    
    elif num == 6:
        
        return 'Sabado'
    
    elif num == 7:
        
        return 'Domingo'
    

def minimo(lista,sucursal):
    
    total = 0
    for i in range(7):
        
        total += lista[sucursal][i]
    
    return total
    