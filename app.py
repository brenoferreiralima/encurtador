from flask import Flask, render_template
import requests, json

app = Flask(__name__)

@app.route("/")
def index():
    link = encurtador("https://www.encurtador.dev/")
    return render_template("index.html", link=link)


# recebe uma URL e retorna uma URL encurtada
def encurtador(url):
    url = url
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
    
    return result