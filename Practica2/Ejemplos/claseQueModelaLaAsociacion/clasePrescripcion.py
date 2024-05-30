# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

class Prescripcion:

    __fecha: str
    __diagnostico: str
    __medicacion: str
    __presentacion: str
    __dosis: str
    __paciente: object
    __medico: object

    def __init__(self, fecha, diagnostico, medicacion, presentacion, dosis, medico, paciente):
    
        self.__fecha=fecha
        self.__diagnostico=diagnostico
        self.__medicacion=medicacion
        self.__presentacion=presentacion
        self.__dosis=dosis
        self.__medico=medico
        self.__paciente=paciente
        self.__medico.addPrescipcion(self)
        self.__paciente.addPrescripcion(self)
