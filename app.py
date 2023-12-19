from flask import Flask, render_template

app = Flask(__name__, static_folder= "static", template_folder= "templates")

@app.route("/")
def index():
    return render_template("index.html", context={})

@app.route("/sindicato")
def sindicato():
    return render_template("sindicato.html", context={})