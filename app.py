from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder= "static", template_folder= "templates")

@app.route("/")
def index():
    return render_template("index.html", context={})

@app.route("/sindicato")
def sindicato():
    return render_template("sindicato.html", context={})

@app.route("/convenios")
def convenios():
    return render_template("convenios.html", context={})

@app.route("/convenios/<pagina>")
def convenios_detalhes(pagina):
    paginas = ["beleza", "comercio", "educacao", "lazer", "saude", "viagem"]
    if pagina in paginas:
        return render_template(f"convenios/{pagina}.html", context={})
    return redirect(url_for("index"))

@app.route("/convencoes")
def convencoes():
    return render_template("convencoes.html", context={})

@app.route("/noticias")
def noticias():
    return render_template("noticias.html", context={})

@app.route("/carteirinha")
def carteirinha():
    return render_template("carteirinha_virtual.html", context={})

@app.route("/contato")
def contato():
    return render_template("contato.html", context={})