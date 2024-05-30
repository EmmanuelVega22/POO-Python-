# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseRegistroCivil import RegistroCivil
from clasePersona import Persona

if __name__=='__main__':

    registro = RegistroCivil('Registro Cuarta Zona', 'Av. Córdoba y Urquiza')
    persona = Persona(20112113, 'Carlos', 'Vargas')
    persona1 = Persona(3444222, 'Anastacia', 'Arboleda')
    registro.inscribirPersona(persona, '28/01/2019')
    registro.inscribirPersona(persona1, '28/01/2019')
    registro.mostrarActas()