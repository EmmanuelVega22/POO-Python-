"""
app.py:
    
@author: Emmanuel
"""

from flask import Flask, render_template, request,redirect,url_for,jsonify,session
from datetime import datetime
import random

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Repartidor,Sucursal,Paquete,Transporte,Repartidor


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

'''
FUNCIONALIDAD 1
'''

@app.route('/bienvenida',methods = ['POST', 'GET'])
def bienvenida():
    

    if request.method == 'POST':
            
        if request.form['texto_dni'] and request.form['texto_nro_repartidor']:
                
            datosform = request.form
                 
            dni = request.form['texto_dni']
            nro_repartidor = request.form['texto_nro_repartidor']

            tipo_usuario = Repartidor.query.filter_by(dni=dni, numero=nro_repartidor).first()

            if tipo_usuario == None:
                     
                return render_template('sesion.html',band= False)
                                
            else: 
                    
                return render_template('bienvenidaRepartidor.html', datos = datosform,hora=datetime.now().hour)
                
@app.route('/bienvenidaDespachante')
def sucursales():
    
    todas_sucursales = Sucursal.query.all()
    return render_template('bienvenidaDespachante.html', sucursales=todas_sucursales)



@app.route('/principalDespachante/<int:sucursal_id>')
def principalDespachante(sucursal_id):
    return render_template('principalDespachante.html', sucursal_id=sucursal_id)


'''
FUNCIONALIDAD 2
'''
@app.route('/despachante_registrar_paquete/<int:sucursal_id>')
def despachante_registrar_paquete(sucursal_id):
    
    sucursales = Sucursal.query.all()
    
    return render_template('despachanteRegistrarPaquete.html',sucursales = sucursales,sucursal_id=sucursal_id)

@app.route('/registrar_paquete', methods=['POST', 'GET'])
def registrar_paquete():
    if request.method == 'POST':
        
        try:
            
            peso = request.form['peso']
            nom_destino = request.form['nomdestinatario']
            dir_destino = request.form['dirdestinatario']
            id_sucursal_remitente = request.form['id_sucursal_destino']
            
            if not peso or not nom_destino or not dir_destino or not id_sucursal_remitente: 
                
                return render_template('despachanteRegistrarPaquete.html',band = False,error = 'Todos los campos son obligatorios.',sucursal_id=id_sucursal_remitente)
            
            else:   
                
                numero_envio = generar_numero_envio()

                
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
                
                return render_template('despachanteRegistrarPaquete.html', band = True,sucursal_id=id_sucursal_remitente)
            
        except Exception as e:
            
            print("Entro al Exception")
            return render_template('despachanteRegistrarPaquete.html',band = False,error = str(e),sucursal_id=id_sucursal_remitente) 
        
'''
FUNCIONALIDAD 3
'''
@app.route('/despachanteSalidaTransporte/<int:sucursal_id>')
def salidaTransporte(sucursal_id):
    todas_sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    return render_template('despachanteSalidaTransporte.html', sucursales=todas_sucursales,sucursal_id = sucursal_id)

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
                
                return render_template('despachanteListaPaquetes.html', band=True,sucursal_id=sucursal_id)
            except Exception as e:
                return render_template('despachanteListaPaquetes.html', paquetes=Paquete.query.all(), band=False, error=str(e),sucursal_id=sucursal_id)
        else:
            return render_template('despachanteListaPaquetes.html', paquetes=Paquete.query.all(), band=False, error="No se seleccionaron paquetes.",sucursal_id=sucursal_id)


'''
FUNCIONALIDAD 4
'''

@app.route('/seleccionar_transporte/<int:sucursal_id>')
def seleccionar_transporte(sucursal_id):
    transportes = Transporte.query.filter_by(fechahorallegada=None, idsucursal=sucursal_id).all()
    return render_template('despachanteLlegadaTransporte.html', transportes=transportes, sucursal_id=sucursal_id)

@app.route('/llegada_transporte', methods=['GET', 'POST'])
def llegada_transporte():
    
    if request.method == 'POST':
       
        sucursal_id = request.form['sucursal_id']

        try:
          
            transportes_seleccionados = request.form.getlist('transportes')
           
            if transportes_seleccionados:
               
                for transportenumero in transportes_seleccionados:
                  
                    transporte = Transporte.query.filter_by(numerotransporte=transportenumero).first()
                   
                    if transporte:
                        
                        transporte.fechahorallegada = datetime.now()
               
                db.session.commit()
                
                return render_template('despachanteLlegadaTransporte.html',band = True,sucursal_id=sucursal_id)
            
            else:
               
                return render_template('despachanteLlegadaTransporte.html',band = True, error="No se seleccionaron transportes.",sucursal_id=sucursal_id)
        
        except Exception as e:
           
            #transportes = Transporte.query.filter_by(fechahorallegada=None).all()
            return render_template('despachanteLlegadaTransporte.html', band = False,error=str(e),sucursal_id=sucursal_id)    


'''
FUNCIONALIDAD 5
'''

@app.route('/seleccionar_repartidor/<int:sucursal_id>')
def seleccionar_repartidor(sucursal_id):
    repartidores = Repartidor.query.filter_by(idsucursal=sucursal_id).all()
    
    paquetes = Paquete.query.filter_by(entregado=False,idrepartidor=0).all()
    return render_template('despachanteAsignarRepartidor.html', repartidores=repartidores, paquetes=paquetes, sucursal_id=sucursal_id)


@app.route('/asignar_repartidor', methods=['GET', 'POST'])
def asignar_repartidor():
    
    if request.method == 'POST':
       
        sucursal_id = request.form['sucursal_id']
        repartidor_id = request.form['repartidor_id']
        try:
          
            repartidor_seleccionados = request.form.getlist('repartidores')
           
            paquetes_seleccionados = request.form.getlist('paquetes')
            
            repartidor = Repartidor()
            
            if repartidor_seleccionados and paquetes_seleccionados:
               
                for numeropaquete in paquetes_seleccionados:
                    
                    paquete = Paquete.query.filter_by(numeroenvio=numeropaquete).first()

                    if paquete:

                        repartidor.paquetes.append(paquete)
                        paquete.idrepartidor= repartidor_id
               
                db.session.commit()
                
                return render_template('despachanteAsignarRepartidor.html',band = True,sucursal_id=sucursal_id)
            
            else:
               
                return render_template('despachanteAsignarRepartidor.html',band = False, error="No se seleccionaron transportes.",sucursal_id=sucursal_id)
        
        except Exception as e:
           
            #transportes = Transporte.query.filter_by(fechahorallegada=None).all()
            return render_template('despachanteAsignarRepartidor.html', band = False,error=str(e),sucursal_id=sucursal_id)    




if __name__=='__main__':
    
    with app.app_context():
        db.create_all()
    app.run()
   