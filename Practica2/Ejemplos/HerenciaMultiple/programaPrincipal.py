# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseAyudante import Ayudante

if __name__=='__main__':

    print('MRO de la clase Ayudante: ',Ayudante.mro())
    
    ayudante = Ayudante(41223444, 'Juarez', 'Roberto','10/03/2020',9.65, 'LSI',
                        3211, 90,'POO',2500,'Sobresaliente',5)
    
    ayudante.mostrarDatos()
