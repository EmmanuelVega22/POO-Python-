"""
app.py:
    
@author: Emmanuel
"""

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Repartidor,Sucursal,Paquete


@app.route('/')
def saludo():
    
    return render_template('principal.html')    
    
@app.route('/sesion')
def sesion():
    
    return render_template('sesion.html')

@app.route('/bienvenida',methods = ['POST', 'GET'])
def bienvenida():
    

    if request.method == 'POST':
            
        if request.form['texto_dni'] and request.form['texto_nro_repartidor'] and request.form['tipo_usuario']:
                
            datosform = request.form
                
            if request.form['tipo_usuario'].lower() == 'despachante':
                    
                return render_template('bienvenidaDespachante.html',datos=datosform,hora=datetime.now().hour)
                
            elif request.form['tipo_usuario'].lower() == 'repartidor':
                
                dni = request.form['texto_dni']
                nro_repartidor = request.form['texto_nro_repartidor']

                tipo_usuario = Repartidor.query.filter_by(dni=dni, numero=nro_repartidor).all()

                if tipo_usuario == None:
                     
                    return render_template('sesion.html',band= False)
                                
                else: 
                    
                    return render_template('bienvenidaRepartidor.html', datos = datosform,hora=datetime.now().hour)
                
            else:
               return render_template('sesion.html',band= False)

@app.route('/sucursales')
def sucursales():
    
    todas_sucursales = Sucursal.query.all()
    return render_template('sucursales.html', sucursales=todas_sucursales)

@app.route('/despachante_registrar_paquete', methods=['POST', 'GET'])
def despachante_registrar_paquete():
    
    sucursales = Sucursal.query.all()
    
    return render_template('despachanteRegistrarPaquete.html',sucursales = sucursales)

@app.route('/registrar_paquete', methods=['POST', 'GET'])
def registrar_paquete():
    if request.method == 'POST':
        peso = request.form['peso']
        nom_destino = request.form['nomdestinatario']
        dir_destino = request.form['dirdestinatario']
        id_sucursal_remitente = request.form['id_sucursal_destino']
        id_sucursal_receptora = request.form['id_sucursal_receptora']
        
        nuevo_paquete = Paquete(
            peso=peso,
            nom_destino=nom_destino,
            dir_destino=dir_destino,
            entregado='No',
            observaciones='',
            id_sucursal_remitente=id_sucursal_remitente,
            id_sucursal_receptora=id_sucursal_receptora,
            id_transporte=None,
            id_repartidor=None
        )
        
        db.session.add(nuevo_paquete)
        db.session.commit()
        
        #return redirect('/paquetes')

    sucursales = Sucursal.query.all()
    return render_template('registrar_paquete.html', sucursales=sucursales)
    


if __name__=='__main__':
    
    with app.app_context():
        db.create_all()
    app.run()
   