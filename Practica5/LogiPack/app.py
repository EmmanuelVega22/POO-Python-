"""
app.py:
    
@author: Emmanuel
"""

from flask import Flask, render_template, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from models import Repartidor

#from models.paquete import Paquete
#from models.transporte import Transporte
#from models.sucursal import Sucursal

@app.route('/')
def saludo():
    
    return render_template('principal.html')
    #return render_template('principal2.html')
    
    
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
      
if __name__=='__main__':
    
    #EJEMPLO DE MOSTRAR LA BASE DATOS Y COMPROBAR SI ESTA CONECTADA
    '''
    print(app.config['SQLALCHEMY_DATABASE_URI'])

    conn = sqlite3.connect('datos.sqlite3')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM repartidor")
    rows = cursor.fetchall()
    print(rows)
    
    conn.close()
    '''
    
    with app.app_context():
        db.create_all()
    app.run()
   