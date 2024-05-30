# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseEmpresaConstructora import EmpresaConstructora

class Departamento(EmpresaConstructora):
    
    __cant_departamentos: int
    __cant_dormitorios: int
    __num_monoblock: int
    __num_departamento: int
    __piso: int
    
    def __init__(self,localidad,direccion,superficie,cant_departamentos,cant_dormitorios,
                 num_monoblock,num_departamento,piso):
        
        super().__init__(localidad,direccion,superficie)
        
        self.__cant_departamentos = cant_departamentos
        self.__cant_dormitorios = cant_dormitorios
        self.__num_monoblock = num_monoblock
        self.__num_departamento = num_departamento
        self.__piso = piso
        
    
    def __str__(self):
        
        cadena = super().__str__()
        cadena += 'Tipo: Departamento\n'
        cadena += 'Cantidad Departamentos: '+ str(self.__cant_departamentos) + '\n'
        cadena += 'Cantidad Dormitorios: '+ str(self.__cant_dormitorios) + '\n'
        cadena += 'Numero Monoblock: '+ str(self.__num_monoblock) + '\n'
        cadena += 'Numero Departamento: '+ str(self.__num_departamento) + '\n'
        cadena += 'Piso: '+ str(self.__piso) + '\n'
        
        return cadena
    
    def getCantDepartamentos(self):
        
        return self.__cant_departamentos
    
    def getCantDormitorios(self):
        
        return self.__cant_dormitorios
    
    def getNumMonoblock(self):
        
        return self.__num_monoblock
    
    def getNumDepartamento(self):
        
        return self.__num_departamento
    
    def getPiso(self):
        
        return self.__piso
    
    
    def importeDeVenta(self):
        
        precioConstruccion = self.getCantDormitorios() * 17000
        
        importeVenta = self.getSuperficieCubierta() * 15 * precioConstruccion
        
        return importeVenta