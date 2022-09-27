import requests
import json

# url a ser encurtada
url = 'https://google.com'
# url da api do encurtador
url_api = 'https://api.encurtador.dev/encurtamentos'
# json que será enviado a API
payload = {'url':url}
# chave que contém o valor da url encurtada
key = 'urlEncurtada'

result = requests.post(url_api, json=payload)
if result.status_code == 200:
    result = result.json()
    result = result[key]
    
print(result)