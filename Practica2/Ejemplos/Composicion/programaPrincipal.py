# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
import msvcrt

from claseProfesor import Profesor

if __name__=='__main__':
    
    profesor = Profesor(11334441, 'Rodríguez', 'Myriam')
    print(profesor)
    print("self.__cuentasCampus:")
    profesor.mostrar()
    msvcrt.getch()
    del profesor