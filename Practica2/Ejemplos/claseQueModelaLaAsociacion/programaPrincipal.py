# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseMedico import Medico
from clasePaciente import Paciente
from clasePrescripcion import Prescripcion

if __name__=='__main__':
    
    paciente = Paciente(14555699, 'Vergara', 'Andrea')
    medico = Medico(19327881, 1125, 'Clínica Médica','González', 'Jorge')
    prescripcion = Prescripcion('11/01/2020', 'Rinitis', 'Hexaler','10 comprimidos', '1 por día',medico, paciente)
    prescripcion2 = Prescripcion('29/01/2020', 'Otitis', 'CiriaxGotas', 'envase 10 ml', '2 gotas cada 8h',medico, paciente)
    