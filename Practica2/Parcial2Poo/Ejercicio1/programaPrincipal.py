# -*- coding: utf-8 -*-
"""
@author: Emmanuel
"""
from claseNoticia import Noticia

#from claseComponenteNoticia import ComponentesNoticia


if __name__=='__main__':
    
    #ccomponentes = ComponentesNoticia('Titulo de la Noticia','Copete de la Noticia','Cuerpo de la Noticia')
    #cnoticia = Noticia('25/05/24','Jorge Castro',ccomponentes)

    cnoticia = Noticia('25/05/24','Jorge Castro')
    
    cnoticia.mostrar()
    del cnoticia