import requests

url = "https://viacep.com.br/ws/13456721/json/"

dados = requests.get(url)
endereco = dados.json()

print(f"Você mora na {endereco['logradouro']}, no bairro {endereco['bairro']}, na cidade {endereco['localidade']}, no estado de {endereco['estado']}.")