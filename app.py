from flask import Flask, render_template, request
import requests, json


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# recebe uma URL e retorna uma URL encurtada
@app.route("/encurtador", methods=["GET","POST"])
def encurtador():
    if request.method == "POST":
        # url original
        url  = request.form["url"]
        # url da api do encurtador
        api = 'https://api.encurtador.dev/encurtamentos'
        # json que será enviado a API
        payload = {'url':url}
        # chave que contém o valor da url encurtada
        key = 'urlEncurtada'

        result = requests.post(api, json=payload)
        if result.status_code == 200:
            result = result.json()
            result = result[key]
        
    return render_template("encurtador.html",link=result)