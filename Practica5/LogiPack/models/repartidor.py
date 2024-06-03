"""
repartidor.py
@author: USUARIO
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Repartidor(db.Model):
    
    __tablename__= 'repartidor'
    id = db.Column(db.Integer,primary_key=True)
    numero = db.Column(db.Integer,nullable=False)
    nombre = db.Column(db.String(60),nullable=False)
    dni = db.Column(db.String(10),unique=True,nullable=False)
    id_sucursal= db.Column(db.Integer,db.ForeignKey('sucursal.id'))
    paquetes =  db.relationship('Paquete', backref='repartidor', cascade="all,delete-orphan")
    
