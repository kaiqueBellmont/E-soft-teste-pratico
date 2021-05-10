import requests
import json


def buscar_dados():
    request = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio')
    teste = json.loads(request.content)
    nome = teste[0]
    sobrenome = teste[1] + ' ' + teste[2]
    nome_completo = nome + ' ' + sobrenome
    print(nome_completo)
