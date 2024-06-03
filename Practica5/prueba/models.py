# -*- coding: utf-8 -*-
"""
models.py:
    
@author: USUARIO
"""


from __main__ import db

class Repartidor(db.Model):
    
    __tablename__= 'repartidor'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    numero = db.Column(db.Integer,nullable=False)
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

class Paquete(db.Model):
    
    __tablename__ = 'paquete'
    
    id = db.Column(db.Integer,primary_key=True)
    numero_envio = db.Column(db.String(20),unique=True,nullable=False)
    peso = db.Column(db.String(80),nullable=False)
    nom_destino = db.Column(db.String(80),nullable=False)
    dir_destino = db.Column(db.String(80),nullable=False)
    entregado =  db.Column(db.String(80),nullable=False)
    observaciones =  db.Column(db.String(80),nullable=False)
    id_sucursal= db.Column(db.Integer,db.ForeignKey('sucursal.id'))
    id_transporte= db.Column(db.Integer,db.ForeignKey('transporte.id'))
    id_repartidor= db.Column(db.Integer,db.ForeignKey('repartidor.id'))
    
