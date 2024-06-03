"""
app.py:
    
@author: Emmanuel
"""

from flask import Flask, render_template, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

#from models.paquete import Paquete
#from models.transporte import Transporte
#from models.sucursal import Sucursal

def get_repartidor_model():
    from models.repartidor import Repartidor
    return Repartidor

@app.route('/')
def saludo():
    
    return render_template('principal.html')
    #return render_template('principal2.html')
    
    
@app.route('/sesion')
def sesion():
    
    return render_template('sesion.html')

@app.route('/bienvenida',methods = ['POST', 'GET'])
def bienvenida():
    
    Repartidor = get_repartidor_model()

    if request.method == 'POST':
            
        if request.form['texto_dni'] and request.form['texto_nro_repartidor'] and request.form['tipo_usuario']:
                
            datosform = request.form
                
            if request.form['tipo_usuario'].lower() == 'despachante':
                    
                return render_template('bienvenidaDespachante.html',datos=datosform,hora=datetime.now().hour)
                
            elif request.form['tipo_usuario'].lower() == 'repartidor':
                    
                tipo_usuario = Repartidor.query.filter_by(dni= request.form['texto_dni']).first()
                    
                if tipo_usuario == None:
                        
                    return render_template('sesion.html',band= False)
                else:
                        
                    nro_repartidor = Repartidor.query.filter_by(nro_repartidor = request.form['texto_nro_repartidor']).first()
                        
                    if nro_repartidor == None:
                            
                        return render_template('bienvenidaRepartidor.html', datos=datosform,nombre= tipo_usuario.nombre ,hora= datetime.now().hour)
                    else:   
                        return render_template('sesion.html',band= False)
            else:
                    
                return render_template('sesion.html',band= False)
        else:
               return render_template('sesion.html',band= False)
      
if __name__=='__main__':
    
    with app.app_context():
        db.create_all()
        app.run()
   