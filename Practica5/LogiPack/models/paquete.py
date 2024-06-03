"""
paquete.py
@author: USUARIO
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Paquete(db.Model):
    
    __tablename__ = 'paquete'
    
    id = db.Column(db.Integer,primary_key=True)
    numero_envio = db.Column(db.Integer,unique=True,nullable=False)
    peso = db.Column(db.Integer,nullable=False)
    nom_destino = db.Column(db.String(80),nullable=False)
    dir_destino = db.Column(db.String(80),nullable=False)
    entregado =  db.Column(db.String(80),nullable=False)
    observaciones =  db.Column(db.Text)
    id_sucursal= db.Column(db.Integer,db.ForeignKey('sucursal.id'))
    id_transporte= db.Column(db.Integer,db.ForeignKey('transporte.id'))
    id_repartidor= db.Column(db.Integer,db.ForeignKey('repartidor.id'))
    