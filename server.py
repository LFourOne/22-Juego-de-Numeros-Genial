from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = "Shhhhh, stay quiet!"

@app.route("/")
def index():
    aleatorio = random.randint(1, 100)
    session["aleatorio"] = aleatorio
    return render_template("index.html", aleatorio=aleatorio)

@app.route("/mistery", methods=["POST"])
def mistery():
    num_ingresado = int(request.form["number-text"])
    aleatorio = session["aleatorio"]
    resultado = ""
    if num_ingresado < aleatorio:
        resultado = "El número es más alto!"
        color = "red"
    elif num_ingresado > aleatorio: 
        resultado = "El número es más bajo!"
        color = "red"
    else:
        resultado = "Felicidades, has ganado!"
        color = "lightgreen"
    return render_template("index.html", resultado=resultado, color=color)
if __name__== "__main__":
    app.run(debug=True)