from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class LoginForm(FlaskForm):
    dni = StringField('DNI', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Login')

class RegisterPackageForm(FlaskForm):
    peso = FloatField('Peso', validators=[DataRequired()])
    nomdestino = StringField('Nombre Destino', validators=[DataRequired(), Length(max=100)])
    dirdestino = StringField('Dirección Destino', validators=[DataRequired(), Length(max=200)])
    idsucursal = SelectField('Sucursal Destino', coerce=int)
    submit = SubmitField('Registrar Paquete')

# Add forms for other functionalities following the same pattern
