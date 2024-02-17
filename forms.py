from wtforms import Form,validators
from wtforms import StringField,SelectField, RadioField, EmailField, IntegerField

class UsersForm(Form):
    x1=IntegerField('x1')
    y1=IntegerField('y1')
    x2=IntegerField('x2')
    y2=IntegerField('y2')
    res=0
    
class ResistenciasForm(Form):
    colores=[("negro","Negro"),
             ("cafe","Cafe"),
             ("rojo","Rojo"),
             ("naranja","Naranja"),
             ("amarillo","Amarillo"),
             ("verde","Verde"),
             ("azul","Azul"),
             ("violeta","Violeta"),
             ("gris","Gris"),
             ("blanco","Blanco")]
    linea1=SelectField('linea1',choices=colores)
    linea2=SelectField('linea2', choices=colores)
    linea3=SelectField('linea3', choices=colores)
    tolerancia=RadioField('tolerancia',choices=[("dorado","Dorado"),("plata","Plata")])

class DicRegistroForm(Form):
    txtPalaIngles=StringField('Palabra en Inglés',[
        validators.DataRequired(message='el campo es requerido')
    ])
    txtPalaEsp=StringField('Palabra en Español',[
        validators.DataRequired(message='el campo es requerido')
    ])

class DicTraducirForm(Form):
    txtPalATraducir=StringField('Palabra',[
        validators.DataRequired(message='el campo es requerido')
    ])
    idiomaOrigen=RadioField('Idioma Origen',[
        validators.DataRequired(message='el campo es requerido')
    ],
    choices=[("ingles","Inglés"),("espanol","Español")])



class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    apaterno = StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    amaterno = StringField('amaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa un nombre valido')
    ])
    edad = IntegerField('edad', [
       validators.number_range(min=1, max=20, message='valor no valido')
    ])
    email = EmailField('email',[
        validators.Email(message='Ingrese un correo válido')
    ])

