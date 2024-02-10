from wtforms import Form 
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