from flask import Flask, render_template, request
import forms
app = Flask(__name__)


@app.route("/")
def index():
    escuela = "UTL"
    alumnos = ["Mario", "Pedro", "Luis", "David"]
    return render_template("index.html" , escuela = escuela, alumnos = alumnos)



@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/multiplicacion",methods=["GET","POST"])
def multi():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "<h1> la multiplicación es  {}</h1>".format(str(int(num1)*int(num2)))
    
@app.route("/division",methods=["GET","POST"])
def div():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "<h1> la division es  {}</h1>".format(str(int(num1)/int(num2)))

@app.route("/resta",methods=["GET","POST"])
def rest():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "<h1> la resta es  {}</h1>".format(str(int(num1)-int(num2)))
    
@app.route("/suma",methods=["GET","POST"])
def suma():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        print(request.form)
        return "<h1> la suma es  {}</h1>".format(str(int(num1)+int(num2)))
    

@app.route("/cine")
def cine():
    return render_template("cine.html", escuela = "Cinepolis")


@app.route("/calcularTotal",methods=["POST"])
def getTotal():
    if request.method=="POST":
        cantidad = request.form.get("cantidad")
        if request.form.get('tarjetaBool')=="1":
            multPrecio = 1
        else:
            multPrecio = 0.9
        print(multPrecio)
        if int(cantidad)>7:
            res = "no puede comprar más de siete boletos por persona"
        elif int(cantidad)<1:
            res = "no se puede comprar menos de un boleto"
        elif int(cantidad)>5:
            res = str(((int(cantidad)*1200)*0.85)*float(multPrecio))
        elif int(cantidad)>2:
            res = str(((int(cantidad)*1200)*0.90)*float(multPrecio))
        else:
            res = str(int(cantidad)*1200)
        return res
    
@app.route("/distancia",methods=["GET","POST"])
def dist():
    res=""
    alum_form = forms.UsersForm(request.form)
    if request.method=='POST':
        x1=alum_form.x1.data
        y1=alum_form.y1.data
        x2=alum_form.x2.data
        y2=alum_form.y2.data
        res=((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)**0.5
        
    return render_template("distancia.html", form=alum_form, res=res)



if __name__ == "__main__":
    app.run(debug=True)