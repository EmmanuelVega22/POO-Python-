# -*- coding: utf-8 -*-
"""
sucursal.py
@author: USUARIO
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Sucursal(db.Model):
    
    __tablename__ = 'sucursal'
    
    id = db.Column(db.Integer,primary_key=True)
    numero_sucursal = db.Column(db.String(80),unique=True,nullable=False)
    provincia = db.Column(db.String(80),nullable=False)
    localidad = db.Column(db.String(80),nullable=False)
    direccion = db.Column(db.String(80),nullable=False)
    repartidores =  db.relationship('Repartidor', backref='sucursal', cascade="all,delete-orphan")
    paquetes =  db.relationship('Paquete', backref='sucursal', cascade="all,delete-orphan")
    transporte =  db.relationship('Transporte', backref='sucursal', cascade="all,delete-orphan")
