from flask import Flask, render_template, request

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
        return "<h1> la suma es  {}</h1>".format(str(int(num1)+int(num2)))
    

if __name__ == "__main__":
    app.run(debug=True)