# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class ActaNacimiento:
    
    __fechaInscripcion: str
    __numeroLibro: int
    __numeroActa: int
    __persona: object
    __registrocivil: object

    def __init__(self, nroActa, nroLibro, fechaInscripcion, persona, registroCivil):

        self.__numeroActa = nroActa
        self.__numeroLibro = nroLibro
        self.__fechaInscripcion = fechaInscripcion
        self.__persona = persona
        self.__registrocivil = registroCivil
        
    def __str__(self):
        
        cadena = 'Fecha de Inscripcion '+self.__fechaInscripcion+'\n'
        cadena +='Libro: '+str(self.__numeroLibro) + ' Acta: '+str(self.__numeroActa)+'\n'
        cadena+= str(self.__persona)
        return cadena