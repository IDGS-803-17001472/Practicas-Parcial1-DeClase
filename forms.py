from wtforms import Form 
from wtforms import StringField,SelectField, RadioField, EmailField, IntegerField

class UsersForm(Form):
    x1=IntegerField('x1')
    y1=IntegerField('y1')
    x2=IntegerField('x2')
    y2=IntegerField('y2')
    res=0