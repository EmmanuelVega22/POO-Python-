# -*- coding: utf-8 -*-
"""
transporte.py
@author: USUARIO
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Repartidor(db.Model):
    
    __tablename__= 'repartidor'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    dni = db.Column(db.String(20),unique=True,nullable=False)
    id_sucursal= db.Column(db.Integer,db.ForeignKey('sucursal.id'))
    paquetes =  db.relationship('Paquete', backref='repartidor', cascade="all,delete-orphan")
    


class Transporte(db.Model):
    
    __tablename__ = 'transporte'
    
    id = db.Column(db.Integer,primary_key=True)
    numero_transporte = db.Column(db.String(80),unique=True,nullable=False)
    fecha_hora_salida = db.Column(db.DateTime)
    fecha_hora_llegada = db.Column(db.DateTime)
    id_sucursal= db.Column(db.Integer,db.ForeignKey('sucursal.id'))
    paquetes =  db.relationship('Paquete', backref='transporte', cascade="all,delete-orphan")

