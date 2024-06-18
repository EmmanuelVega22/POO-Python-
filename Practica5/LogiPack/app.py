"""
app.py:
    
@author: Emmanuel
"""

from flask import Flask, render_template, request,redirect,url_for,jsonify
from datetime import datetime
import random

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Repartidor,Sucursal,Paquete,Transporte


'''
FUNCIONES
'''

def generar_numero_envio():
    
    ultimo_numero_envio = Paquete.query.order_by(Paquete.numeroenvio.desc()).first()
    
    if ultimo_numero_envio == None:
        
        siguiente_numero_envio = 1000
        
    else:
        
        siguiente_numero_envio = ultimo_numero_envio.numeroenvio + 20
        
    
    return siguiente_numero_envio



'''
APP ROUTE
'''

@app.route('/')
def saludo():
    
    return render_template('principal.html')    
    
@app.route('/sesion')
def sesion():
    
    return render_template('sesion.html')

@app.route('/bienvenida',methods = ['POST', 'GET'])
def bienvenida():
    

    if request.method == 'POST':
            
        if request.form['texto_dni'] and request.form['texto_nro_repartidor']:
                
            datosform = request.form
                 
            dni = request.form['texto_dni']
            nro_repartidor = request.form['texto_nro_repartidor']

            tipo_usuario = Repartidor.query.filter_by(dni=dni, numero=nro_repartidor).all()

            if tipo_usuario == None:
                     
                return render_template('sesion.html',band= False)
                                
            else: 
                    
                return render_template('bienvenidaRepartidor.html', datos = datosform,hora=datetime.now().hour)
                
@app.route('/bienvenidaDespachante')
def sucursales():
    
    todas_sucursales = Sucursal.query.all()
    return render_template('bienvenidaDespachante.html', sucursales=todas_sucursales)

@app.route('/principalDespachante')
def principalDespachante():
    
    
    return render_template('principalDespachante.html')

@app.route('/despachante_registrar_paquete', methods=['POST', 'GET'])
def despachante_registrar_paquete():
    
    sucursales = Sucursal.query.all()
    
    return render_template('despachanteRegistrarPaquete.html',sucursales = sucursales)

@app.route('/registrar_paquete', methods=['POST', 'GET'])
def registrar_paquete():
    if request.method == 'POST':
        
        try:
            
            peso = request.form['peso']
            nom_destino = request.form['nomdestinatario']
            dir_destino = request.form['dirdestinatario']
            id_sucursal_remitente = request.form['id_sucursal_destino']
            numero_envio = generar_numero_envio()
            
            if not peso or nom_destino or dir_destino or id_sucursal_remitente or numero_envio: 
              
                nuevo_paquete = Paquete(
                    numeroenvio = numero_envio,
                    peso=peso,
                    nomdestinatario=nom_destino,
                    dirdestinatario=dir_destino,
                    entregado=False,
                    observaciones='',
                    idsucursal=id_sucursal_remitente,
                    idtransporte=0,
                    idrepartidor=0
                )
                
                db.session.add(nuevo_paquete)
                db.session.commit()
                
                return render_template('despachanteRegistrarPaquete.html', band = True)
            
            else: Exception()
        except Exception as e:
            
            return render_template('despachanteRegistrarPaquete.html',band = False,error = str(e)) 
        
@app.route('/despachanteSalidaTransporte')
def salidaTransporte():
    todas_sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    return render_template('despachanteSalidaTransporte.html', sucursales=todas_sucursales)

@app.route('/seleccionar_paquetes/<int:sucursal_id>')
def seleccionar_paquetes(sucursal_id):
    paquetes = Paquete.query.filter_by(entregado=False, idrepartidor=0).all() #Busca los paquetes que no fueron entregados o que no tiene repartidores asignados
    return render_template('despachanteListaPaquetes.html', paquetes=paquetes, sucursal_id=sucursal_id)

@app.route('/registrar_paquete_transporte', methods=['POST'])
def registrar_paquete_transporte():
    if request.method == 'POST':
        paquetes_seleccionados = request.form.getlist('paquetes')
        sucursal_id = request.form['sucursal_id']
        if paquetes_seleccionados:
            try:
                nuevo_transporte = Transporte(
                    numerotransporte=random.randint(100, 999),
                    fechahorasalida=datetime.now(),
                    fechahorallegada=None,
                    idsucursal=sucursal_id
                )
                
                for numero_envio in paquetes_seleccionados:
                    paquete = Paquete.query.filter_by(numeroenvio=numero_envio).first()
                    if paquete:
                        nuevo_transporte.paquetes.append(paquete)
                
                db.session.add(nuevo_transporte)
                db.session.commit()
                
                return render_template('despachanteListaPaquetes.html', band=True)
            except Exception as e:
                return render_template('despachanteListaPaquetes.html', paquetes=Paquete.query.all(), band=False, error=str(e))
        else:
            return render_template('despachanteListaPaquetes.html', paquetes=Paquete.query.all(), band=False, error="No se seleccionaron paquetes.")


if __name__=='__main__':
    
    with app.app_context():
        db.create_all()
    app.run()
   