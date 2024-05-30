# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""

from claseProvincia import Provincia
from claseGobernador import Gobernador

if __name__=='__main__':
    
    provincia = Provincia('San Juan',681055)
    gobernador = Gobernador(27888111, 'Sergio Uñac', provincia)
    provincia.setGobernador(gobernador)
    print(provincia)