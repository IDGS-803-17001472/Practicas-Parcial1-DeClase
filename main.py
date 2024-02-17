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


reg_form = forms.DicRegistroForm()
trasl_form = forms.DicTraducirForm()

@app.route("/diccionario",methods=["GET","POST"])
def dicc():
    res=""
    archivo_texto=open('nombres.txt','a')
    reg_form = forms.DicRegistroForm(request.form)
    if request.method=='POST'and reg_form.validate():
        txtPalaIngles=reg_form.txtPalaIngles.data
        txtPalaEsp=reg_form.txtPalaEsp.data
        archivo_texto.write("{}:{}\n".format(txtPalaIngles.lower(),txtPalaEsp.lower()))
        archivo_texto.close()
    return render_template("diccionario.html", form1=reg_form, form2=trasl_form, res=res)

@app.route("/obtenerPalabraDiccionario",methods=["POST"])
def diccget():
    trasl_form = forms.DicTraducirForm(request.form)
    res="Palabra no encontrada"
    if request.method=='POST'and trasl_form.validate():
        archivo_texto=open('nombres.txt','r')
        txtPalATraducir=trasl_form.txtPalATraducir.data
        idiomaOrigen=trasl_form.idiomaOrigen.data
        if idiomaOrigen=="ingles":
            idiomaDestino=1
        elif idiomaOrigen=="espanol":
            idiomaDestino=0
        for line in archivo_texto.readlines():
            if( txtPalATraducir.lower() in line):
                res=line.split(":")[idiomaDestino]
        archivo_texto.close()
    return render_template("diccionario.html", form1=reg_form, form2=trasl_form, res=res)



    
@app.route("/resistencias",methods=["GET","POST"])
def resistencia():
    res=""
    tolerancia=""
    toleranciaStr=""
    resMin=""
    linea1=""
    linea2=""
    linea3=""
    resMax=""
    restn_form = forms.ResistenciasForm(request.form)
    if request.method=='POST':
        linea1=restn_form.linea1.data
        linea2=restn_form.linea2.data
        linea3=restn_form.linea3.data
        tolerancia=restn_form.tolerancia.data
        if linea1=="negro":
            nLinea1="0"
        elif linea1=="cafe":
            nLinea1="1"
        elif linea1=="rojo":
            nLinea1="2"
        elif linea1=="naranja":
            nLinea1="3"
        elif linea1=="amarillo":
            nLinea1="4"
        elif linea1=="verde":
            nLinea1="5"
        elif linea1=="azul":
            nLinea1="6"
        elif linea1=="violeta":
            nLinea1="7"
        elif linea1=="gris":
            nLinea1="8"
        elif linea1=="blanco":
            nLinea1="9"
        
        
        if linea2=="negro":
            nLinea2="0"
        elif linea2=="cafe":
            nLinea2="1"
        elif linea2=="rojo":
            nLinea2="2"
        elif linea2=="naranja":
            nLinea2="3"
        elif linea2=="amarillo":
            nLinea2="4"
        elif linea2=="verde":
            nLinea2="5"
        elif linea2=="azul":
            nLinea2="6"
        elif linea2=="violeta":
            nLinea2="7"
        elif linea2=="gris":
            nLinea2="8"
        elif linea2=="blanco":
            nLinea2="9"


        if linea3=="negro":
            nLinea3=1
        elif linea3=="cafe":
            nLinea3=10
        elif linea3=="rojo":
            nLinea3=100
        elif linea3=="naranja":
            nLinea3=1000
        elif linea3=="amarillo":
            nLinea3=10000
        elif linea3=="verde":
            nLinea3=100000
        elif linea3=="azul":
            nLinea3=1000000
        elif linea3=="violeta":
            nLinea3=10000000
        elif linea3=="gris":
            nLinea3=100000000
        elif linea3=="blanco":
            nLinea3=1000000000
        toleranciaVal=0
        toleranciaStr = tolerancia
        print(tolerancia)
        if tolerancia=="dorado":
            toleranciaVal=0.05 
        elif tolerancia=="plata":
            toleranciaVal=0.1
        
        lineaTotal= nLinea1 + nLinea2


        res=int(lineaTotal)*nLinea3
        resMin=res*(1-toleranciaVal)
        resMax=res*(1+toleranciaVal)
        tolerancia = tolerancia + " " + str(toleranciaVal*100)+"%"
        
    return render_template("resistencias.html", form=restn_form, res=res, resMin=resMin,resMax=resMax, col1=linea1, col2=linea2, col3=linea3, tolerancia=tolerancia, toleranciaStr=toleranciaStr)



if __name__ == "__main__":
    app.run(debug=True)