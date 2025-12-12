import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", page="home")

@app.route("/stabilimento-balneare")
def stabilimento():
    return render_template("stabilimento.html", page="stabilimento")

@app.route("/ristorante-di-pesce")
def ristorante():
    return render_template("ristorante.html", page="ristorante")

@app.route("/lounge-bar")
def lounge():
    return render_template("lounge.html", page="lounge")

@app.route("/contatti")
def contatti():
    return render_template("contatti.html", page="contatti")

if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
